import sys
print(f"{sys.maxsize = }")


cities = []  # empty list   (or cities = list() )
cities = ['Portland', 'Pittsburg', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)  # append each element of more_cities
print(f"cities: {cities}\n")
junk = [10, 20, 30]
cities.extend(junk)
cities.append(junk)
print(f"{cities = }")


# LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)
cities[0] = "Framingham"
# cities[99] = "Miami" fails because there are not 100 elements in the list

del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")
