from prueba1 import dameUnNUmero
import pytest

def test_prueba1():
    assert dameUnNUmero(2) == 4

pytest.main(["-v", "--tb=line", "-rN", __file__])