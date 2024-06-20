from django.shortcuts import render,get_object_or_404,redirect
from galeria.models import Fotografia
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuário não logado")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografica").filter(publicada=True)
    return render(request, 'galeria/index.html',{"cards" : fotografias})


def imagem(resquest, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(resquest, 'galeria/imagem.html',{"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuário não logado")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografica").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, "galeria/buscar.html", {"cards" : fotografias})
