from django.shortcuts import render
import stripe
from django.views.decorators.csrf import csrf_exempt
from config.settings import base
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import json
import stripe
from django.core.exceptions import ObjectDoesNotExist

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Invoice
from reportlab.lib.pagesizes import letter
import requests
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode


from django.utils import timezone
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

# Create your views here.




@csrf_exempt
def create_checkout_session(request, price):

    stripe.api_key = base.STRIPE_SECRET_KEY

    try:
       checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": 'USD',
                    "product_data": {
                        "name": "plans",
                    },
                    "unit_amount": int(price),
                },
                "quantity": 1,
            }
        ],

        mode="payment",
        customer_creation='always',
        success_url=base.DOMAIN_NAME,
        cancel_url=base.DOMAIN_NAME,
        )

       return JsonResponse({'success': True, 'checkout_session_id': checkout_session.id})

    except Exception as e:
       return Response(
          {'error': 'somthing went wrong when creating stripe checkout_session' },
          status=status.HTTP_500_INTERNAL_SERVER_ERROR
       )


def generate_invoice_pdf(session):

    receiptEmail= session['receipt_email']
    amount_total = session['amount']
    currency = session['currency']

    buffer = BytesIO()

    p = canvas.Canvas(buffer)


    p.setFont("Helvetica-Bold", 16)
    rgb_color = (255/255, 111/255, 125/255)
    p.setFillColorRGB(*rgb_color)
    p.drawCentredString(300, 780, "Smartovate Plan Invoice")

    p.setFont("Helvetica-Oblique", 12)
    p.setFillColor(colors.black)

    p.drawString(100, 710,f"Receipt Email: {receiptEmail}")
    p.drawString(100, 690, f"Amount Total: {amount_total} {currency}")

    rgb_color = (128/255,128/255,128/255)
    p.setFillColorRGB(*rgb_color)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, 650, f"Congratulations on successfully registering as a customer with Smartovate")

    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(100, 630, f"Please print/record this information and keep in a safe place.")


    welcome_paragraph = (
        "Thank you for choosing Smartovate! \n We are thrilled to welcome you to our Plan.\n"
        "Your gateway to a world of cutting-edge tools and services designed to elevate your organization \n"
        "to new heights. We are excited to embark on this journey with you, offering a suite of innovative \n"
        "solutions crafted to enhance  productivity, real-time collaboration, and fortify the security of \n"
        "your operations.\n"

        "If you have any questions or need assistance,  please feel free to reach out to our support team."

    )


    p.setFillColor(colors.black)

    x, y, width, height = 100, 610, 500, 90
    text_object = p.beginText(x, y)
    text_object.setFont("Helvetica", 11)

    lines = welcome_paragraph.split('\n')

    for line in lines:
        text_object.textLine(line)

    p.drawText(text_object)

     # Add a border around the entire page
    border_width = 1  # You can adjust the border width as needed
    page_width, page_height = p._pagesize
    p.setFillColor(colors.black)
    p.setLineWidth(border_width)
    p.rect(border_width / 2, border_width / 2, page_width - border_width, page_height - border_width)


    p.showPage()
    p.save()

    buffer.seek(0)
    pdf_content = buffer.getvalue()

    return pdf_content

@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = base.STRIPE_ENDPOINT_SECRET

    payload = request.body
    sig_header = request.headers.get('Stripe-Signature', None)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except stripe.error.SignatureVerificationError as e:

        print('Invalid signature:', e)
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    if event['type'] == 'payment_intent.succeeded':
        session = event['data']['object']

        # Retrieve the session ID from the session
        session_id = session['id']
        receiptEmail= session['receipt_email']
        amount_total = session['amount']
        currency = session['currency']

        invoice = Invoice(token=session_id, receipt_email=receiptEmail, amount=amount_total,currency=currency)
        invoice.save()

        #encode session_id
        token = urlsafe_base64_encode(force_bytes(session_id))
        print("my token is:",token)

        #  generate the PDF content
        pdf_content = generate_invoice_pdf(session)

        invoices_pdf = 'invoices'
        if not os.path.exists(invoices_pdf):
           os.makedirs(invoices_pdf)

         # Save the PDF content to a file
        pdf_invoice = os.path.join(invoices_pdf,f'Smartove_invoice_{session_id}.pdf')
        with open(pdf_invoice, 'wb') as pdf_file:
            pdf_file.write(pdf_content)

        #email content
        subject = 'Invoice for your purchase'
        body = f'''Thank you for your purchase! Here is your invoice for {amount_total} {currency}
        https://dev.app.smartovate.com/landing-page?token={token}'''
        from_email = 'support@smartovate.com'
        to_email = [receiptEmail]

        email = EmailMessage(
            subject,
            body,
            from_email,
            to_email,
              )
        email.attach_file(pdf_invoice)
        try:
              email.send()
              print("Email sent successfully")
        except Exception as e:
              print(f"Error sending email: {e}")


    elif event['type'] == 'payment_intent.payment_failed':

        session = event['data']['object']
        receiptEmail= session['receipt_email']

        if receiptEmail:
            # Send an email to the customer about the payment failure
            subject = 'Payment Failed for Your Purchase'
            body = 'We regret to inform you that your payment has failed. Please check your payment details and try again.'
            from_email = 'support@smartovate.com'
            to_email =session['receipt_email']

            email = EmailMessage(
            subject,
            body,
            from_email,
            to_email,
        )
        email.send()

    return HttpResponse(status=200)


@csrf_exempt
def webhook(request, received_token):
    try:
        # Decode the received token
        decoded_token = urlsafe_base64_decode(received_token)
        decoded_token_str = decoded_token.decode()
       # Retrieve the invoice using the decoded token
        invoice = Invoice.objects.get(token=decoded_token_str)

        #Prepare the response data
        response_data = {
            'success': True,
            'message': 'Token is valid',
            'receipt_email': invoice.receipt_email,
            'amount_total': invoice.amount,
            'currency': invoice.currency,
        }

        return JsonResponse(response_data)

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Invalid token'}, status=400)



