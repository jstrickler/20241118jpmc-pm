name = "John jacob jingleheimer schmidt"

print("name: ", name)
print("upper: ", name.upper())
print("title: ", name.title())

j_count = name.lower().count('j')
print("j count:", j_count)

print("len:", len(name))  # name.__len__() WRONG!!

print("position of 'jacob':", name.find('jacob'))

