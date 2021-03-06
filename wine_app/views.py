
from django.shortcuts import render, redirect
from .models import Wine, PostImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.db.models import Sum
from cart.cart import Cart
from .forms import UserProfileForm, ExtendedUserCreationForm


def welcome(request):
    return render(request, 'base.html')

def whitewine(request):
    white_wines = Wine.objects.filter(wine_category__name="alb")
    template_name = 'wine.html'
    context = {
        'wines' : white_wines,
        'type':'alb',
    }
    
    return render (request, template_name, context)

def redwine(request):
    red_wines = Wine.objects.filter(wine_category__name="rosu")
    template_name = 'wine.html'
    context = {
        'wines' : red_wines,
        'type':'rosu',
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


class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine_detail.html'
    context_object_name = 'wine'


def shopping_cart(request):
    a = Cart(request)
    total = 0
    for key,value in a.cart.items():
        total += float(value['price']) * value['quantity']
    return render(request, 'shopping_cart.html', {'total': total})


def shopping_cart_contact(request):
    a = Cart(request)
    total = 0
    for key,value in a.cart.items():
        total += float(value['price']) * value['quantity']
    return render(request, 'shopping_cart_contact.html', {'total': total})


def cart_add(request, id):
    cart = Cart(request)
    product = Wine.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect("/shopping_cart") 


def item_clear(request, id):
    cart = Cart(request)
    product = Wine.objects.get(id=id)
    cart.remove(product)
    return redirect("/shopping_cart")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("welcome")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'registration/register.html', context)


def logout(request):
    return render(request, 'registration/logout.html')
