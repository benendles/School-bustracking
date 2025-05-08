from django.db import models

# Create your models here.
class Extractedimage(models.Model):
    image = models.ImageField(upload_to='extracted_images/')
    extracted_text = models.TextField()

    def __str__(self):
        return f"Extracted Image {self.id}"