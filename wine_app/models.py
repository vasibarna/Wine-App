from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name    


class Wine(models.Model):
    name = models.CharField(max_length=110)
    description = models.TextField(default="null")
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    note = models.FloatField()
    image = models.ImageField(upload_to='images', default="null")
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
        new_height = 900
        new_width  = new_height * width / height
        output_size = (new_width, new_height)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def __str__(self):
        return f'Pictures for: <<{self.wine}>>'



