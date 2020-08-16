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
    path('detail/<int:pk>', views.WineDetailView.as_view(), name='wine_detail'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('shopping_cart/', views.shopping_cart, name = 'shopping_cart'),
    path('shopping_cart_contact/', views.shopping_cart_contact, name = 'shopping_cart_contact'),
]


