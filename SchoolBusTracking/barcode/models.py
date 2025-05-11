from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File 
from PIL import Image, ImageDraw


# Create your models here.
class Extractedimage(models.Model):
    image = models.ImageField(upload_to='extracted_images/')
    extracted_text = models.TextField()
class Website (models.Model):
    name = models.CharField(max_length=100)
    qr_code = models.ImageField(upload_to='qr_codes' , blank=True, null=True)


    def __str__(self):
        return f"Extracted Image {self.id}-{self.name}"

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        qrcode_img = qrcode_img.convert('RGB')
        canvas = Image.new('RGB',  (qrcode_img.size[0], qrcode_img.size[1]), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code_{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)  
        canvas.close()
        super().save(*args, **kwargs)
