from django.db import models

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.TextField()  # Field to store the encoded session_id
    receipt_email = models.EmailField(default='')
    amount = models.CharField(max_length=50,default='')
    currency = models.CharField(max_length=3, default='USD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.token}"
