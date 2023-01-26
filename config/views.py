from django.shortcuts import render


def index(request):
    frase = 'Index Sheik Jalim Rabei'
    return render(request, 'index.html', {'frase': frase})
