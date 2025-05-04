from django.shortcuts import render,redirect
from .form import BusTicketForm
from .models import BusTicket
from .util import extract_amount_from_receipt, generate_qr_code


def receipt(request):
    return render(request,'receipt.html')

def submit_ticket(request):
    if request.method == 'POST':
        form = BusTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            extracted_amount = extract_amount_from_receipt(ticket.receipt_photo.path)

            if extracted_amount and abs(extracted_amount - float(ticket.payment_amount)) < 0.01:
                ticket.is_verified = True
                qr_data = f"{ticket.name};{ticket.passport_photo.url}"
                qr_file = generate_qr_code(qr_data)
                ticket.qr_code.save(f"{ticket.name}_qr.png", qr_file)

            ticket.save()
            return redirect('ticket_success')
    else:
        form = BusTicketForm()
    return render(request, 'receipt.html', {'form': form})
    