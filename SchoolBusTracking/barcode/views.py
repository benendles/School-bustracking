import pytesseract
from PIL import Image
from django.shortcuts import  render,redirect
from  .models import Extractedimage
from .forms import ExtractedimageForm
pytesseract.pytesseract.tesseract_cmd = '/opt/anaconda3/envs/tesseract-env/bin/tesseract'
def upload_and_extract(request):
    if request.method == 'POST':
        print("Form submitted!")  # Debugging
        form = ExtractedimageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid!")  # Debugging
            uploaded_image = form.save(commit=False)
            try:
                image = Image.open(uploaded_image.image)
                print("Image opened successfully!")  # Debugging
                uploaded_image.extracted_text = pytesseract.image_to_string(image)
                print("Extracted Text:", uploaded_image.extracted_text)  # Debugging
                uploaded_image.save()
                return redirect('result', pk=uploaded_image.pk)
            except Exception as e:
                print("Error during OCR:", e)  # Debugging
                return render(request, 'upload.html', {'form': form, 'error': 'Error during OCR processing.'})
        else:
            print("Form is not valid!")  # Debugging
    else:
        form = ExtractedimageForm()
    return render(request, 'upload.html', {'form': form})

def result_view(request, pk):
    image_entry = Extractedimage.objects.get(pk=pk)
    return render(request, 'result.html', {'image_entry': image_entry})



    