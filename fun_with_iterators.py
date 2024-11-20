colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in colors:
    print(color)
print()

colors_enum = enumerate(colors)
print(f"{colors_enum = }")
for i, color in colors_enum:
    print(i, color)
print()

for i, color in enumerate(colors):
    print(i, color)
print()

food_list = ['duck', 'tofu', 'candy']
food_rev = reversed(food_list)
print(f"{food_list = }")
print(f"{food_rev = }")
for food in food_rev:
    print(food)

# range(stop-before)  range(start-at, stop-before)
# range(start-at, stop-before, count-by)

for i in range(5):
    print(i)
print()

for i in range(1, 11):
    print(i, i * '*')

r = range(100)
print(f"{len(r) = }")
print(f"{r[5] = }")
print(f"{type(r) = }")
wow = range(10000000)
print(wow)
print(len(wow))