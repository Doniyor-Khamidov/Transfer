from django.shortcuts import render

from transfer.models import Transfer
from main.models import *
from transfer.models import *


def home_view(request):
    return render(request, 'index.html')

def clubs_view(request):
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'clubs.html', context)

def latest_transfers_view(request):
    last_season= Season.objects.order_by('name').last()
    transfers = Transfer.objects.filter(season=last_season).order_by('-price')
    context = {
        'transfers': transfers,
        'last_season': last_season

    }
    return render(request, 'latest-transfers.html', context)