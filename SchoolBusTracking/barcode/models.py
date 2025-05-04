from django.db import models

# Create your models here.

class BusTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to login user
    name = models.CharField(max_length=100)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    passport_photo = models.ImageField(upload_to='passports/')
    receipt_photo = models.ImageField(upload_to='receipts/')
    is_verified = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qrcodes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)