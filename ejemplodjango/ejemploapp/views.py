from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    respu = "<ul>"
    respu = respu + "<li>Elemento 1</li>"
    respu = respu + "<li>Elemento 2</li>"
    respu = respu + "</ul>"

    return HttpResponse("<center><h1>Hola mundo<h1></center>" + respu)

def nuevococinero(request):
    return HttpResponse("<p>Esta es la paguina del nuevo cocinero</p>")

    
def consultarpedido(request):
    return HttpResponse("<p>Consultar pedido</p>")

def gato(request):
    return HttpResponse("<p>Hola gato</p>")

def pato(request):
    return HttpResponse("<p>Hola pato</p>")

def vaca(request):
    return HttpResponse("<p>Hola vaca</p>")
