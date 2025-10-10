from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('clubs/', clubs_view, name='clubs'),
    path('clubs/<int:pk>/', club_retrieve_view, name='club-info'),
    path('latest_transfers/', latest_transfers_view, name='latest_transfers'),
    path('players/', players_view, name='players'),
    path('tryouts/', tryouts_view, name='tryouts'),
    path('about/', about_view, name='about'),
    path('U_20_players/',u20_players_view, name='u20_players'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)