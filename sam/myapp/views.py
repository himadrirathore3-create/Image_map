from django.shortcuts import render

def govt(request):
    return render(request, 'govt.html')

def map(request):
    return render(request, 'map.html')

def show(request):
    return render(request, 'show.html')

def station(request):
    return render(request, 'station.html')

def theatre(request):
    return render(request, 'theatre.html')