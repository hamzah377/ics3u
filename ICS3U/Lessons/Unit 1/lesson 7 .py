import math

# Input for x and y
x = input("Please input a whole number between 1 and 20: ")
x = int(x)
y = input("Please input another nonzero whole number between 1 and 20: ")
y = int(y)

# Check if both x and y are within the allowed range
if not (1 <= x <= 20) or not (1 <= y <= 20):
    print("Error: Both x and y must be between 1 and 20.")
else:
    # Check if y is zero before performing modulo operation
    if y == 0:
        print("Error: You cannot divide by zero.")
    else:
        print(f"Now deciding if {y} is a factor of {x}...")
        rem = x % y
        if rem == 0:
            print(f"Yes! {y} is a factor of {x}")
        else:
            print(f"No, {y} is not a factor of {x}")
