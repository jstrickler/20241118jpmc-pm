colors = list()    # list colors = new list();
colors.append('pink')
colors.append('purple')
colors.append('puce')
colors.insert(2, 'green')

states = list()
states.append('NC')
states.append("FL")
states.append("ND")

print(f"{states[1] = }")

class Dog: # object
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()
d3.bark()
print(f"{d1 = }")
