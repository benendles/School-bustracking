from django.db import models

# Create your models here.
class Expected_info (models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.CharField(max_length=100)

class Receipt(models.Model):
    image = models.ImageField(upload_to='receipts/')

class Barcode(models.Model):
    image = models.ImageField(upload_to='receipts/',default='upload your passport photo')
