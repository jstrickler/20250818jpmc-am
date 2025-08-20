raw_celsius_temperature = input("Enter the temperature in Celsius: ")
celsius_temperature = float(raw_celsius_temperature)
fahrenheit_temperature = ((9 * celsius_temperature) / 5 ) + 32
print(f"{celsius_temperature}\u00B0 C is {fahrenheit_temperature}\u00B0 F")