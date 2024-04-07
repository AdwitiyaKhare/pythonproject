from django.urls import path
from . import views

urlpatterns = [
    path('', views.nse_future_list, name='nse_future_list'),  # URL for listing NSE futures
    path('<int:future_id>/', views.nse_future_detail, name='nse_future_detail'),  # URL for viewing NSE future details
]
