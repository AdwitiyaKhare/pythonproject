from django.urls import path
from . import views

urlpatterns = [
    path('', views.trades_list, name='trades_list'),  # URL for listing trades
    path('<int:trade_id>/', views.trade_detail, name='trade_detail'),  # URL for viewing trade details
]
