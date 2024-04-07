from django.shortcuts import render
from django.http import HttpResponse

def mcx_future_list(request):
    # Logic to fetch and display a list of MCX futures
    return HttpResponse("List of MCX futures")  # Placeholder response

def mcx_future_detail(request, future_id):
    # Logic to fetch and display details of a specific MCX future
    return HttpResponse(f"MCX future details for Future ID: {future_id}")  # Placeholder response
