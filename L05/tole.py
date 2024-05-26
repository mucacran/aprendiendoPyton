import math
from pytest import approx

def test_sqrt():
    # Calculamos la raíz cuadrada de 5
    actual_value = math.sqrt(5)
    
    # Definimos el valor esperado
    expected_value = 2.23606797749979
    
    # Usamos approx para verificar si actual_value está cerca de expected_value
    assert actual_value == approx(expected_value, rel=0.01)

if __name__ == "__main__":
    test_sqrt()
    print("Todos los tests pasaron!")
