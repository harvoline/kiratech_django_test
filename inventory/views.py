from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import requests
import os

# Create your views here.


def index(request):
    response = requests.get('http://127.0.0.1:8020/api/inventory')
    response.raise_for_status()

    return render(request, 'inventory/index.html', {'inventories': response.json()})


def show(request, inventory_id):

    response = requests.get(f'http://127.0.0.1:8020/api/inventory/{inventory_id}')
    response.raise_for_status()

    return render(request, 'inventory/show.html', {'inventory': response.json()})

