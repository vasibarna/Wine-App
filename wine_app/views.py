from .models import Vin
from django.shortcuts import render
from django.views.generic import ListView

def bineativenit(request):
    return render(request, 'base.html')

def vinalb(request):
    vinuri_albe = Vin.objects.all()
    template_name = 'vin.html'
    context = {
        'vinuri' : vinuri_albe,
        'tip':'alb'
    }
    return render (request, template_name, context)

def vinrosu(request):
    vinuri_rosii = Vin.objects.all()
    template_name = 'vin.html'
    context = {
        'vinuri' : vinuri_rosii,
        'tip':'rosu'
    }
    return render (request, template_name, context)

def vinrose(request):
    vinuri_rose = Vin.objects.all()
    template_name = 'vin.html'
    context = {
        'tip':'rose',
        'vinuri' : vinuri_rose,
    }
    return render (request, template_name, context)

def sampanie(request):
    sampanii = Vin.objects.all()
    template_name = 'vin.html'
    context = {
        'vinuri' : sampanii,
        'tip':'sampanie'
    }
    return render (request, template_name, context)
def vinaniversar(request):
    aniversar = Vin.objects.all()
    template_name = 'vin.html'
    context = {
        'vinuri' : aniversar,
        'tip':'aniversar'
    }
    return render (request, template_name, context)

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload_image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})