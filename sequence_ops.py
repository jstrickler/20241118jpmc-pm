flags = [True] * 10
print(f"{flags = }")

print('-' * 60)
print(f"{'Python! ' * 5 = }")

a = "butter"
b = "milk"
c = a + b
print(f"{c = }")

print(f"{len(c) = }")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{sorted(fruits) = }")
print()
print(f"{min(fruits) = }")
print(f"{max(fruits) = }")

values = [5, 8, 27, -3, 14, 98, 5.6]
print(f"{sum(values) = }")

for fruit in fruits:
    print(fruit)
