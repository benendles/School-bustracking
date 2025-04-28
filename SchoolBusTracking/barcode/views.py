from django.shortcuts import render

# Create your views here.
def receipt(request):
    return render(request,'receipt.html')