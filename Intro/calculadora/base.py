
def sumar(a, b):
    return a + b

def restar(a , b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a // b

def elevar(base, exponente):
    if exponente >= 1:
        return elevar(base, exponente -1) * base
    else:
        return 1
