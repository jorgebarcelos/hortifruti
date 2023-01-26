from django.shortcuts import render


def index(request):
    frase = 'index de produto'
    return render(request, 'produto/index.html', {'frase': frase})


def pagina1(request):
    frase = 'pagina1 de produto'
    return render(request, 'produto/pagina1.html', {'frase': frase})


def pagina2(request):
    frase = 'pagina2 de produto'
    return render(request, 'produto/pagina2.html', {'frase': frase})
