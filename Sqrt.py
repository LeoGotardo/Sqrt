from math import sqrt

def inverte_sinal(pri):
    pri =  pri * -1
    return pri

def soma(pri, sec):
    sum = pri + sec
    return sum

def subtracao(pri, sec):
    sub = pri - sec
    return sub

def multiplicacao(pri, sec):
    mult = pri * sec 
    return mult

def divisao(pri, sec):
    div = pri / sec
    return div

def quadrado(pri):
    pri = pri * pri
    return pri

def raiz(pri):
    raiz = sqrt(pri)
    return raiz

def delta(a, b, c):
    return subtracao(quadrado(b), multiplicacao(multiplicacao(4, a), c))


def bhaskara():
    a = float(input(f"a:"))
    b = float(input(f"b:"))
    c = float(input(f"c:"))

    r1 = divisao(
        soma(inverte_sinal(b), raiz(delta(a, b, c))),
        multiplicacao(2, a))

    r2 = divisao(
        subtracao(inverte_sinal(b), raiz(delta(a, b, c))),
        multiplicacao(2, a))

    print('Para a equação: ', a, 'x^2 + ', b, 'x + ', c, ' = 0')
    print('As raizes são: ', r1, ' e ', r2)


bhaskara()
