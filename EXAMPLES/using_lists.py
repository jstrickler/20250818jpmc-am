colors = [] # empty
animals = list()  # empty list
cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")
print(f"{len(cities) = }")
print(f"{cities[0] = }")


cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # for city in more_cities: cities.append(city)
print(f"cities: {cities}\n")

# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3] 
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()  # pops last element
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)  #pops by index
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)    