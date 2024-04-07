from django.urls import path
from . import views

urlpatterns = [
    path('', views.cds_future_list, name='cds_future_list'),  # URL for listing CDS futures
    path('<int:future_id>/', views.cds_future_detail, name='cds_future_detail'),  # URL for viewing CDS future details
]
