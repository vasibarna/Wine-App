from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('whitewine/', views.whitewine, name = 'whitewine'),
    path('redwine/', views.redwine, name='redwine'),
    path('rosewine/', views.rosewine, name='rosewine'),
    path('champagne/', views.champagne, name='champagne'),
    path('anniversary/', views.anniversary, name='anniversary'),
    path('upload/', views.image_upload_view),

]