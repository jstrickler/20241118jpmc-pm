fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print(f"{f0 = }\n")

#  [VALUE-TO-APPEND for VAR in ITERABLE if CONDITION ...]
f1 = [f.upper() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
f2 = []
for f in fruits:
    if f.startswith('p'):
        f2.append(f.upper())

print(f"{f2 = }\n")

f3 = [f for f in fruits if f.startswith('p')]
print(f"{f3 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [(p[0], p[1].upper()) for p in people]
print(f"{last_names = }\n")

last_names_gen = (p[1] for p in people)  # use () instead of [] to make an iterator AKA generator
print(f"{last_names_gen = }\n")
for last_name in last_names_gen:
    print(last_name)

fruit_lengths = {f:len(f) for f in fruits}
print(f"{fruit_lengths = }\n")

dobs = {(p[0], p[1]):p[-1] for p in people}
print(f"{dobs = }\n")

