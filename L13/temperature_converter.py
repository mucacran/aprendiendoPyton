"""
Temperature Converter
Author: Sergio
Date: [Current Date]

This program provides functions to convert temperatures between Celsius, Fahrenheit, and Kelvin.
To run the program, simply import the functions and call them with the desired temperature values.
"""

def convert_celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    :param celsius: Temperature in degrees Celsius.
    :return: Temperature in degrees Fahrenheit.
    """
    return celsius * 9/5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    :param fahrenheit: Temperature in degrees Fahrenheit.
    :return: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 5/9

def convert_celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    :param celsius: Temperature in degrees Celsius.
    :return: Temperature in Kelvin.
    """
    return celsius + 273.15

def convert_kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    :param kelvin: Temperature in Kelvin.
    :return: Temperature in degrees Celsius.
    """
    return kelvin - 273.15

def convert_fahrenheit_to_kelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin.
    :param fahrenheit: Temperature in degrees Fahrenheit.
    :return: Temperature in Kelvin.
    """
    return (fahrenheit - 32) * 5/9 + 273.15

def convert_kelvin_to_fahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit.
    :param kelvin: Temperature in Kelvin.
    :return: Temperature in degrees Fahrenheit.
    """
    return (kelvin - 273.15) * 9/5 + 32

def convert_fahrenheit_to_kelvin(fahrenheit):
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    return convert_celsius_to_kelvin(celsius)

def convert_kelvin_to_fahrenheit(kelvin):
    celsius = convert_kelvin_to_celsius(kelvin)
    return convert_celsius_to_fahrenheit(celsius)

def get_conversion_input():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the current unit (C/F/K): ").upper()
    target_unit = input("Enter the target unit (C/F/K): ").upper()
    return temp, unit, target_unit

def display_conversion_results(original_temp, original_unit, converted_temp, converted_unit):
    print(f"{original_temp}°{original_unit} is equal to {converted_temp:.2f}°{converted_unit}")

def main():
    original_temp, original_unit, target_unit = get_conversion_input()
    
    if original_unit == "C" and target_unit == "F":
        converted_temp = convert_celsius_to_fahrenheit(original_temp)
    elif original_unit == "F" and target_unit == "C":
        converted_temp = convert_fahrenheit_to_celsius(original_temp)
    elif original_unit == "C" and target_unit == "K":
        converted_temp = convert_celsius_to_kelvin(original_temp)
    elif original_unit == "K" and target_unit == "C":
        converted_temp = convert_kelvin_to_celsius(original_temp)
    elif original_unit == "F" and target_unit == "K":
        converted_temp = convert_fahrenheit_to_kelvin(original_temp)
    elif original_unit == "K" and target_unit == "F":
        converted_temp = convert_kelvin_to_fahrenheit(original_temp)
    else:
        print("Invalid unit conversion.")
        return

    display_conversion_results(original_temp, original_unit, converted_temp, target_unit)

if __name__ == "__main__":
    main()
