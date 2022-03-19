from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Player'})   # The plan is to change player to actual name dynamically

def add_info(request):
    val1 = request.GET['name']
    val2 = request.GET['campaign']
    val3 = request.GET['date']
    res = val1
    res2 = val2
    res3 = val3
    return render(request, 'result.html', {'name': res, 'campaign': res2, 'date': res3})