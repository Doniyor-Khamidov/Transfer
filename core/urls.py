from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from transfer.views import *

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
    path('stats/', stats_view, name='stats'),
    path('stats/150-accurate-predictions/',stats_top_150_accurate_prediction, name='top150'),
    path('stats/transfer-records/', transfer_record_view, name = 'transfer-record'),
    path('stats/top-50-clubs-by-expenditure-in-2025/',top_50_expend_view, name='top50-expend'),
    path('stats/top-50-clubs-by-income-in-2025/',top_50_income_view, name='top50-income'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)