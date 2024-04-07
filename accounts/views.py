from django.shortcuts import render
from django.http import HttpResponse

def account_list(request):
    # Logic to fetch and display a list of accounts
    return HttpResponse("List of accounts")  # Placeholder response

def account_detail(request, account_id):
    # Logic to fetch and display details of a specific account
    return HttpResponse(f"Account details for Account ID: {account_id}")  # Placeholder response
