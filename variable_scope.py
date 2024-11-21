
COLOR = "red"  # global (file)

def spam():
    COLOR = "blue"
    animal = "elk"  # local
    print(f"{animal = }")
    print(f"{COLOR = }")

spam()
print(f"{COLOR = }")
