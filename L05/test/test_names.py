from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sergio","Bravo") == "Bravo; Sergio"

def test_extract_family_name():
    assert extract_family_name("Bravo; Sergio") == "Bravo"

def test_extract_given_name():
    assert extract_given_name("Bravo; Sergio") == "Sergio"


# Llame a la función principal que forma parte de pytest para que la 
# computadora ejecute las funciones de prueba en este archivo. 
pytest.main([ "-v" , "--tb=line" , "-rN" , __file__])
