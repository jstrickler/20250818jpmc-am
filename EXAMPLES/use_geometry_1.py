import sys
#        pkg.pkg.module
import alpha.mathlib.geometry as geometry  # load geometry.py

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module import search rules
# 1. current folder
# 2. folders in PYTHONPATH
# 3. installation folder or subfolders

print(f"{sys.prefix = }")
print()
for path in sys.path:
    print(path)
