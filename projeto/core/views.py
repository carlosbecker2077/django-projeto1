from django.shortcuts import render

# Create your views here.
from .models import Produto

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader


def index(request):
    print(dir(request))
    print(f"Método: {request.method}")
    print(f"Headers: {request.headers['User-Agent']}")
    print(f"User: {request.user}")
    print(f"dir do User: {dir(request.user)}")

    if request.user.is_anonymous:
        usuario = 'Usuário não logado'
    else:
        usuario = f'Usuário logado: {request.user}'

    produtos = Produto.objects.all()

    context = {
        'bolota': 'bolota',
        'mama': 'mamaaaaaaama',
        'youtube': 'https://www.youtube.com/',
        'usuario': usuario,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def erro404(request, exeption):
    template = loader.get_template('erro404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def erro500(request):
    template = loader.get_template('erro500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
