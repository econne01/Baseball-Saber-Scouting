from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from scouter.models import Player

def index(request):
    test_var = 'This string is a test variable'
    context = {'var': test_var}
    return render(request, 'scouter_index.html', context)

def contact(request):
    return render(request, 'contact.html')

def games(request):
    return render(request, 'games.html')

class BatterDetail(TemplateView):
    model = Player
    
    