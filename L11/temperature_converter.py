def celsius_to_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convierte grados Celsius a Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convierte grados Kelvin a Celsius"""
    return kelvin - 273.15

def main():
    print("Convertidor de Unidades de Temperatura")
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"{celsius} °C es {celsius_to_fahrenheit(celsius):.2f} °F")
    print(f"{celsius} °C es {celsius_to_kelvin(celsius):.2f} K")

if __name__ == "__main__":
    main()
