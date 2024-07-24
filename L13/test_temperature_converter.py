import pytest
from temperature_converter import (
    convert_celsius_to_fahrenheit,
    convert_fahrenheit_to_celsius,
    convert_celsius_to_kelvin,
    convert_kelvin_to_celsius,
    convert_fahrenheit_to_kelvin,
    convert_kelvin_to_fahrenheit
)

def test_convert_celsius_to_fahrenheit():
    """
    Test conversion from Celsius to Fahrenheit.
    """
    assert convert_celsius_to_fahrenheit(0) == pytest.approx(32, rel=1e-9)
    assert convert_celsius_to_fahrenheit(100) == pytest.approx(212, rel=1e-9)
    assert convert_celsius_to_fahrenheit(-40) == pytest.approx(-40, rel=1e-9)

def test_convert_fahrenheit_to_celsius():
    """
    Test conversion from Fahrenheit to Celsius.
    """
    assert convert_fahrenheit_to_celsius(32) == pytest.approx(0, rel=1e-9)
    assert convert_fahrenheit_to_celsius(212) == pytest.approx(100, rel=1e-9)
    assert convert_fahrenheit_to_celsius(-40) == pytest.approx(-40, rel=1e-9)

def test_convert_celsius_to_kelvin():
    """
    Test conversion from Celsius to Kelvin.
    """
    assert convert_celsius_to_kelvin(0) == pytest.approx(273.15, rel=1e-9)
    assert convert_celsius_to_kelvin(100) == pytest.approx(373.15, rel=1e-9)
    assert convert_celsius_to_kelvin(-273.15) == pytest.approx(0, rel=1e-9)

def test_convert_kelvin_to_celsius():
    """
    Test conversion from Kelvin to Celsius.
    """
    assert convert_kelvin_to_celsius(273.15) == pytest.approx(0, rel=1e-9)
    assert convert_kelvin_to_celsius(373.15) == pytest.approx(100, rel=1e-9)
    assert convert_kelvin_to_celsius(0) == pytest.approx(-273.15, rel=1e-9)

def test_convert_fahrenheit_to_kelvin():
    """
    Test conversion from Fahrenheit to Kelvin.
    """
    assert convert_fahrenheit_to_kelvin(32) == pytest.approx(273.15, rel=1e-9)
    assert convert_fahrenheit_to_kelvin(212) == pytest.approx(373.15, rel=1e-9)
    assert convert_fahrenheit_to_kelvin(-459.67) == pytest.approx(0, rel=1e-9)

def test_convert_kelvin_to_fahrenheit():
    """
    Test conversion from Kelvin to Fahrenheit.
    """
    assert convert_kelvin_to_fahrenheit(273.15) == pytest.approx(32, rel=1e-9)
    assert convert_kelvin_to_fahrenheit(373.15) == pytest.approx(212, rel=1e-9)
    assert convert_kelvin_to_fahrenheit(0) == pytest.approx(-459.67, rel=1e-9)

if __name__ == "__main__":
    pytest.main()
