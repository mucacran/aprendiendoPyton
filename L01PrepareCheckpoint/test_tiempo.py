from tiempo import cels_from_fahr


import sys

# Agregamos la ruta al directorio site-packages de tu instalación de Python al sys.path
sys.path.append(r'C:\Users\MUCACRAN\AppData\Roaming\Python\Python311\site-packages\_pytest')

# Importamos approx desde pytest
import pytest
from _pytest import approx

def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating-point numbers.
    """
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)

# Llamamos a la función main de pytest para que el
# equipo ejecute las funciones de prueba en este archivo.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])

"""
python -m pip install --user --upgrade pip setuptools wheel
"""