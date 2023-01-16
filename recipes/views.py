from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.


def home(request):
    # return HTTP RESPONSE
    return HttpResponse('HOME')


def contato(request):
    # return HTTP RESPONSE
    return HttpResponse('CONTATO')


def sobre(request):
    # return HTTP RESPONSE
    return HttpResponse('SOBRE')
