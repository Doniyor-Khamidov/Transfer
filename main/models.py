from django.db import models
from django.core.validators import MinValueValidator


class Country(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='clubs')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):

    name = models.CharField(max_length=255)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    number = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=255)
    nation = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])


    def __str__(self):
        return self.name