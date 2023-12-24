#!/usr/bin/python3

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

def celcius_to_fahrenheit(celcius):
    return ((celcius * 1.8) + 32)

def fahrenheit_to_celcius(fahrenheit):
    return ((fahrenheit - 32) * (5/9))

def convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed for the same unit

    # Call the appropriate conversion function based on units
    # Tuple that contains the units at range
    conversion_functions = {
        ('meters', 'kilometers'): meters_to_kilometers,
        ('kilometers', 'meters'): kilometers_to_meters,
        ('feet', 'meters'): feet_to_meters,
        ('meters', 'feet'): meters_to_feet,
        ('miles', 'kilometers'): miles_to_kilometers,
        ('kilometers', 'miles'): kilometers_to_miles,
        ('celcius', 'fahrenheit'): celcius_to_fahrenheit,
        ('fahrenheit', 'celcius'): fahrenheit_to_celcius,
    }

    conversion_key = (from_unit.lower(), to_unit.lower())
    if conversion_key in conversion_functions:
        return conversion_functions[conversion_key](value)
    else:
        print("Invalid units or conversion not supported.")
        return None

def main():
    print()
    # Get user input
    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the unit to convert from: ")
    to_unit = input("Enter the unit to convert to: ")

    #This snippet performs the conversion
    result = convert(value, from_unit, to_unit)

    # Displays the result
    if result is not None:
        print(f"{value} {from_unit.capitalize()} is equal to {result:.4f} {to_unit.capitalize()}.")

if __name__ == "__main__":
    main()
