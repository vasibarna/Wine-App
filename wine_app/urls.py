from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bineativenit, name='bineativenit'),
    path('vinalb/', views.vinalb, name = 'vinalb'),
    path('vinrosu/', views.vinrosu, name='vinrosu'),
    path('vinrose/', views.vinrose, name='vinrose'),
    path('sampanie/', views.sampanie, name='sampanie'),
    path('vinaniversar/', views.vinaniversar, name='vinaniversar'),
    path('upload/', views.image_upload_view),

]