from django.db import models

class Categorie(models.Model):
    nume = models.CharField(max_length = 30)
    def __str__(self):
        return self.nume

class Vin(models.Model):
    nume = models.CharField(max_length=110)
    descriere = models.TextField(default="null")
    cantitate = models.IntegerField(default=1)
    imagine = models.CharField(default="null",max_length=110)
    categorie = models.ForeignKey('wine_app.Categorie',on_delete=models.DO_NOTHING)
    pret = models.FloatField()
    nota = models.FloatField()
    def __str__(self):
        return f'{self.nume} at {self.pret} lei with image {self.imagine} and category {self.categorie} has a rating of {self.nota}.'

class Picture(models.Model):
    vin_id = models.ForeignKey('wine_app.Vin',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50) 
    picture = models.ImageField(upload_to='images', default="null")

    def __str__(self):
        return self.vin_id
    