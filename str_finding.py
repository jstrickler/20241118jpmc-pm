import re
s = "this paper is the paperiest paper I have ever papered"

pos = s.find("paper")
print(f"{pos = }")

pos = s.find("paper", pos + 1)
print(f"{pos = }")


pos = s.rfind("paper")
print(f"{pos = }")

for m in re.finditer("paper", s):
    print(m.start())