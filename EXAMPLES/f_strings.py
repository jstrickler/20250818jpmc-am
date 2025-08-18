city = 'Orlando'
temperature = 85
hit_count = 5
average = 3.4563892382

# f"xxx"  f'xxx'  f"""xxx""" f'''xxx'''
# variables inserted into string
print(f"It is {temperature}\u00B0 F in {city}")
print()

# :03d means format (decimal) integer in 3 characters, 
#      left-padded with zeros
# :.2f means round a float to 2 decimal points
print(f"hit count is {hit_count:03d} average is {average:.2f} (original {average})")
print()

# any expression is OK
print(f"2 + 2 is {2 + 2}")

 