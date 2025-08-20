import sys

raw_celsius_temp = sys.argv[1]
celsius_temp = float(raw_celsius_temp)
fahr_temp = ((9 * celsius_temp) / 5) + 32
print(f"{celsius_temp}\u00B0 C is {fahr_temp}\u00B0 F")