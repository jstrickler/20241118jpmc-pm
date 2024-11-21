import EXAMPLES.alpha.mathlib.geometry as geometry  # find geometry.py and run its code
import sys
import re

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# 1. current folder
# 2. folders in PYTHONPATH
# 3. installation folder + "lib"  (sys.prefix + "lib")
print(f"{sys.prefix = }\n")

print(f"{sys.modules['re'] = }")
print(f"{sys.modules['geometry'] = }")
print()
for path in sys.path:
    print(path)
