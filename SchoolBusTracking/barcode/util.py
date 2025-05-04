from PIL import Image
import pytesseract
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import re

def extract_amount_from_receipt(receipt_path):
    text = pytesseract.image_to_string(Image.open(receipt_path))
    match = re.search(r'\d+\.\d{2}', text)
    return float(match.group()) if match else None

def generate_qr_code(data):
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue())