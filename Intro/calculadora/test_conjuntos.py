from base_conjuntos import *

def test_suma_conjuntos():
    x = [2,2,2,4,2]
    assert 12 == sumar(x)

def test_suma_conjuntos_recursiva():
    x = [2, 2, 2, 4, 2]
    assert 12 == sumar_recursivo(x)