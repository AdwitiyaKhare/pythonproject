from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='account_list'),  # URL for listing accounts
    path('<int:account_id>/', views.account_detail, name='account_detail'),  # URL for viewing account details
]
