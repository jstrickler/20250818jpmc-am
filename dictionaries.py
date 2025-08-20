d1 = {}  # empty dict
d2 = dict() # same
state_info = {
    'NC': 'Raleigh',
    'TN': 'Nashville',
    'NY': 'Albany',
}
print(f"{state_info['NY'] = }")
state_info['CA'] = 'Sacramento'
print(f"{state_info = }\n")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
print(f"{airports['MCO'] = }")
if 'WAW' in airports:
    print(f"{airports['WAW'] = }")
# print(f"{airports['WAW'] = }")  # raises error

print(f"{airports.get('WAW') = }")
print(f"{airports.get('WAW', 'NOT FOUND') = }")

print(f"{airports.setdefault('WAW', 'Warsaw') = }")
print(f"{airports = }")
print(f"{airports['WAW'] = }")
print()

for code, city in airports.items():
    print(code, city)
print()
