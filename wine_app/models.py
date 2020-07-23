from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Categorie(models.Model):
    nume = models.CharField(max_length = 30)
    def __str__(self):
        return self.nume

class Vin(models.Model):
    nume = models.CharField(max_length=110)
    descriere = models.TextField(default="null")
    cantitate = models.IntegerField(default=1)
    categorie = models.ForeignKey('wine_app.Categorie',on_delete=models.DO_NOTHING)
    pret = models.FloatField()
    nota = models.FloatField()
    def __str__(self):
        return f'{self.nume} at {self.pret} lei with category {self.categorie} has a rating of {self.nota}.'

class Picture(models.Model):
    vin = models.ForeignKey('wine_app.Vin',on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to='images', default="null")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        width, height = img.size
        new_height = 900
        new_width  = new_height * width / height
        output_size = (new_width, new_height)
        img.thumbnail(output_size)
        img.save(self.picture.path)


