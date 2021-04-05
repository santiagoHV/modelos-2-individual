import base

def sumar(lista):
    acum = 0

    for i in lista:
        acum = base.sumar(acum, i)

    return acum

def sumar_recursivo(lista):

    if lista == []:
        return 0

    return sumar_recursivo(lista[1:]) + lista[0]

def pasar_enteros(lista):

    enteros = []

    for i in lista:
        enteros.append(int(i))

    return enteros