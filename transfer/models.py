from django.db import models
from django.db.models import ForeignKey
from main.models import *

class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    player = ForeignKey(Player, on_delete=models.CASCADE)
    old_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='export_transfers')
    new_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='import_transfers')
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    price_tft = models.FloatField(validators=[MinValueValidator(0.0)],blank = True, null = True)
    date = models.DateField(blank = True, null = True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name}: {self.old_club.name} - {self.new_club.name}"