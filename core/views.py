from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.html import format_html


def _result(title, value_a, value_b, result):
    return HttpResponse(
        format_html('<h1>{}: {} e {} = {}</h1>', title, value_a, value_b, result)
    )


def hello(request, nome, idade):
    return HttpResponse(format_html('<h1>Hello {} de {} anos</h1>', nome, idade))


def soma(request, valor_a, valor_b):
    return _result('Soma', valor_a, valor_b, valor_a + valor_b)


def multiplicacao(request, valor_a, valor_b):
    return _result('Multiplicação', valor_a, valor_b, valor_a * valor_b)


def divisao(request, valor_a, valor_b):
    if valor_b == 0:
        return HttpResponseBadRequest('O divisor não pode ser zero.')
    return _result('Divisão', valor_a, valor_b, valor_a / valor_b)


def subtracao(request, valor_a, valor_b):
    return _result('Subtração', valor_a, valor_b, valor_a - valor_b)
