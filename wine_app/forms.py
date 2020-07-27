from django import forms
from .models import PostImage


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = PostImage
        fields = ('wine', 'image1', 'image2', 'image3')