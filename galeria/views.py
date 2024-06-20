from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def imagem(resquest):
    return render(resquest,'galeria/imagem.html')