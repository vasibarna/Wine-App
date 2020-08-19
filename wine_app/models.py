from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name    


class Wine(models.Model):
    name = models.CharField(max_length=110)
    description = models.TextField(default="Vin recomandat")
    sugar_content = models.CharField(max_length=20, default="Demisec")
    year = models.IntegerField(default=2015)
    price = models.FloatField()
    note = models.FloatField()
    image = models.ImageField(upload_to='images', default="null")
    quantity = models.IntegerField(default=10)
    wine_category = models.ForeignKey('wine_app.Category',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'


class PostImage(models.Model):
    wine = models.ForeignKey(Wine, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', default="null")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width, height = img.size
        print(width, height)
        new_height = 900
        new_width  = int(new_height * width / height)
        output_size = (new_width, new_height)
        a = img.resize(output_size)
        a.save(self.image.path)
        print(new_width, new_height)

    def __str__(self):
        return f'Pictures for: <<{self.wine}>>'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    city = models.CharField(max_length=110)
    street = models.CharField(max_length=110)
    number = models.CharField(max_length=110)
    phone_number = models.CharField(max_length=110)

    def __str__(self):
        return self.user.username



