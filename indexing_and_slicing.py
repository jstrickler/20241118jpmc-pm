fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava']

print(f"{fruits[0] = }")
print(f"{fruits[len(fruits)-1] = }")
print(f"{fruits[-1] = }")
#  start-at:stop-before
#  start-at:stop-before:count-by
print(f"{fruits[2:7] = }")
print(f"{fruits[3:5] = }")
print(f"{fruits[:6] = }")
print(f"{fruits[6:] = }")
print(f"{fruits[-5:] = }")  # last 5

singer = "Ariana Grande"
start = 3
stop = 6
print(f"{singer[start:stop] = }")
print()

a = [1, 2, 3]
a.append(4)
print(f"{a = }")
b = a  # not a real copy, just an alias
b.append(5)
print(f"{a = }")
print(f"{b = }")
c = list(a)  # separate copy
a.append(6)
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")

# m = [1, 2, 3]
# foo(m)

print(f"{a = }")
print(f"{2 + 2 = }")
