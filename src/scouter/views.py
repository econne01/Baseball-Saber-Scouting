from django.shortcuts import render

def index(request):
    test_var = 'This string is a test variable'
    context = {'var': test_var}
    return render(request, 'scouter_index.html', context)

def contact(request):
    return render(request, 'contact.html')

def games(request):
    return render(request, 'games.html')
