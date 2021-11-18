from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))

def soma(request, valor_a, valor_b):
    soma = valor_a + valor_b
    return HttpResponse('<h1>A soma entre {} e {} = {}<h1>'.format(valor_a, valor_b, soma))

def multiplicacao(request, valor_a, valor_b):
    multiplicacao = valor_a * valor_b
    return HttpResponse('<h1>A Multiplicacao entre {} e {} = {}<h1>'.format(valor_a, valor_b, multiplicacao))

def divisao(request, valor_a, valor_b):
    divisao = valor_a / valor_b
    return HttpResponse('<h1>A divisao entre {} e {} = {}<h1>'.format(valor_a, valor_b, divisao))

def subtracao(request, valor_a, valor_b):
    subtracao = valor_a - valor_b
    return HttpResponse('<h1>A subtracao entre {} e {} = {}<h1>'.format(valor_a, valor_b, subtracao))