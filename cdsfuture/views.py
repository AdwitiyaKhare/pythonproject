from django.shortcuts import render
from django.http import HttpResponse

def cds_future_list(request):
    # Logic to fetch and display a list of CDS futures
    return HttpResponse("List of CDS futures")  # Placeholder response

def cds_future_detail(request, future_id):
    # Logic to fetch and display details of a specific CDS future
    return HttpResponse(f"CDS future details for Future ID: {future_id}")  # Placeholder response
