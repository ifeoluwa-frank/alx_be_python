FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

what_to_convert = float(input("Enter the temperature to convert: "))
current_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if current_unit == "C":
    result = convert_to_fahrenheit(what_to_convert)
    print(f"{what_to_convert}°C is {result}°F")
elif current_unit == "F":
    result = convert_to_celsius(what_to_convert)
    print(f"{what_to_convert}°F is {result}°C")