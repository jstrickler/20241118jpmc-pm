from EXAMPLES.card import Card

value = 123.234293293
first_name = "Barnabus"
city = "Mumbai"

print(value, first_name, city)  # value + SP + value + SP + value + NL
print("Python is your friend")

print(value, first_name, city, sep="")
print(value, first_name, city, sep="/")
print(value, first_name, city, sep=", ")

print(first_name, end=", ")
print(city)
print()
print()
print("hello")

# city: first_name

print(f"{city}: {first_name}")
print(f"{first_name} lives in {city}")

print(f"value is {value}")
print(f"{value = }")

print(f"value is >{value:.4f}<")

print(f"{city = }")

print(str(city))
print(repr(city))

print(f"{city = }")


c = Card("8", "Diamonds")
print(c)  # str()
print(repr(c))

print(f"{c = }")

print(f"{Card = }")

#            c
print("c is {} value is {:.4f}".format(c, value))


# ancient history
print("c is %s value is %.4f" % (c, value))



