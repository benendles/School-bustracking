from django import forms
from .models import BusTicket

class BusTicketForm(forms.ModelForm):
    class Meta:
        model = BusTicket
        fields = ['name', 'payment_amount', 'passport_photo', 'receipt_photo']