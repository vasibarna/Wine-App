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
    wine_category = models.ForeignKey('wine_app.Category',on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return f'{self.name}'


class PostImage(models.Model):
    wine = models.ForeignKey(Wine, default=None, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images', default="null")
    image2 = models.ImageField(upload_to='images', default="null")
    image3 = models.ImageField(upload_to='images', default="null")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image1.path)
        width, height = img.size
        new_height = 900
        new_width  = new_height * width / height
        output_size = (new_width, new_height)
        img.thumbnail(output_size)
        img.save(self.image1.path)

        img = Image.open(self.image2.path)
        width, height = img.size
        new_height = 900
        new_width  = new_height * width / height
        output_size = (new_width, new_height)
        img.thumbnail(output_size)
        img.save(self.image2.path)

        img = Image.open(self.image3.path)
        width, height = img.size
        new_height = 900
        new_width  = new_height * width / height
        output_size = (new_width, new_height)
        img.thumbnail(output_size)
        img.save(self.image3.path)

    def __str__(self):
        return f'Pictures for: <<{self.wine}>>'



