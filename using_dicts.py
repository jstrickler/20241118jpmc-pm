d1 = {}   # best practice
d2 = dict()  # not as good...

d3 = {'first_name': 'Bruce', 'last_name': 'Willis'}
d3['movies'] = []
d3['movies'].append("Die Hard")
d3['movies'].append("The Fifth Element")
print(f"{d3 = }\n")


airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['MCO'] = }")
print(f"{airports['RDU'] = }")
airports['RDU'] = 'Durham'
print(f"{airports = }\n")
# print(f"{airports['VCE'] = }")
print(f"{airports.get('VCE') = }")
print(f"{airports.get('VCE', 'Venice') = }")
print(f"{airports = }\n")
print(f"{airports.setdefault('VCE', 'Venice') = }")
print(f"{airports = }\n")
for code in 'RDU', 'ORD', 'XYZ', "VCE", "ROM":
    print(f"{code} {code in airports = }")
print()


genders = {'m': 'male', 'f': 'female'}

for code, city in airports.items():
    print(code, city)  # genders[gender]
print()

