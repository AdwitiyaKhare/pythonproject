from django.urls import path
from . import views

urlpatterns = [
    path('', views.mcx_future_list, name='mcx_future_list'),  # URL for listing MCX futures
    path('<int:future_id>/', views.mcx_future_detail, name='mcx_future_detail'),  # URL for viewing MCX future details
]
