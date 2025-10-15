from django.db.models import Sum
from django.db.models import F, ExpressionWrapper, Func
from django.shortcuts import render
from .models import *

def latest_transfers_view(request):
    last_season = Season.objects.order_by('name').last()
    transfers = Transfer.objects.filter(season=last_season).order_by('-price')
    context = {
        'transfers': transfers,
        'last_season': last_season
    }
    return render(request, 'latest-transfers.html', context)

def stats_view(request):
    return render(request, 'stats.html')

def stats_top_150_accurate_prediction(request):
    class Round(Func):
        function = 'ROUND'
        template = '%(function)s(%(expression)s, 2)'

    transfers = Transfer.objects.annotate(
        accurate_prediction=ExpressionWrapper(
            Round(
                Func(
                    (F('price') - F('price_tft')) / F('price_tft') * 100,
                    function='ABS'
                ),
            ),
            output_field=models.FloatField()
        )
    ).order_by('accurate_prediction')

    context = {
        'transfers': transfers,
    }

    return render(request, 'stats/150-accurate-predictions.html', context)

def transfer_record_view(request):
    transfers = Transfer.objects.all()

    context = {
        'transfers': transfers,
    }

    return render(request, 'stats/transfer-records.html', context)

def top_50_expend_view(request):
    clubs = (
        Transfer.objects
        .values('new_club__name')
        .annotate(total_spent=Sum('price'))
        .order_by('-total_spent')[:50]
    )

    context = {
        'clubs': clubs,
    }

    return render(request, 'stats/top-50-clubs-by-expenditure-in-2025.html', context)

def top_50_income_view(request):
    clubs = (
        Transfer.objects
        .values('old_club__name')
        .annotate(total_income=Sum('price'))
        .order_by('-total_income')[:50]
    )

    context = {
        'clubs': clubs,
    }

    return render(request, 'stats/top-50-clubs-by-income-in-2025.html', context)
