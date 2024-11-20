
import sys   # Import the sys module 

print(sys.argv) # Print all parameters, including script itself

print(f"{sys.argv[0] = }")

x = 5
print(f"{x = }")


name = sys.argv[1]  # Get the first actual parameter
print("name is", name)
