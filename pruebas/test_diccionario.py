import pytest
import arreglo as ar

array = [5,3,4,2,1]
diccionario = [
    {"nombre":"Lupita","edad":18},
    {"nombre":"Andy","edad":35},
    {"nombre":"Marlen","edad":15}]

def test_diccionario():
    assert ar.ordenar(array) == [1,2,3,4,5]
def test_mayores():
    assert ar.personas_mayores(diccionario) == 2