from .models import *
from django.db.models import Count

def get_countries_context(request):
    countries = Country.objects.annotate(
        club_count=Count('club')
    ).order_by('-club_count')

    context = {
        'countries': countries
               }

    return context