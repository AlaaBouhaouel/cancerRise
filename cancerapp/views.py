from django.shortcuts import render


def landing(request):
    return render(request, 'cancerapp/landing.html')


def login_view(request):
    return render(request, 'cancerapp/login.html')


def home(request):
    return render(request, 'cancerapp/home.html')


def water(request):
    return render(request, 'cancerapp/water.html')


def feelings(request):
    return render(request, 'cancerapp/feelings.html')


def alert(request):
    return render(request, 'cancerapp/alert.html')

def chatbot(request):
    return render(request, 'cancerapp/chatbot.html')

def settings(request):
    return render(request, 'cancerapp/settings.html')