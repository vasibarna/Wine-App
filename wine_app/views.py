from .models import Wine
from django.shortcuts import render
from django.views.generic import ListView

def welcome(request):
    return render(request, 'base.html')

def whitewine(request):
    white_wines = Wine.objects.filter(wine_category__name="alb")
    template_name = 'wine.html'
    context = {
        'wines' : white_wines,
        'type':'alb'
    }
    return render (request, template_name, context)

def redwine(request):
    red_wines = Wine.objects.filter(wine_category__name="rosu")
    template_name = 'wine.html'
    context = {
        'wines' : red_wines,
        'type':'rosu'
    }
    return render (request, template_name, context)

def rosewine(request):
    rose_wines = Wine.objects.filter(wine_category__name="rose")
    template_name = 'wine.html'
    context = {
        'type':'rose',
        'wines' : rose_wines,
    }
    return render (request, template_name, context)

def champagne(request):
    champagnes = Wine.objects.filter(wine_category__name="sampanie")
    template_name = 'wine.html'
    context = {
        'wines' : champagnes,
        'type':'sampanie'
    }
    return render (request, template_name, context)

def anniversary(request):
    anniversaries = Wine.objects.filter(wine_category__name="aniversar")
    template_name = 'wine.html'
    context = {
        'wines' : anniversaries,
        'type':'aniversar'
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