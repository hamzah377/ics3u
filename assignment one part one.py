# Part 1: Even or odd detector

print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

# Take input from the user
first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

# Check if the first number is even or odd
if first_number % 2 == 0:
    first_is_even = True
else:
    first_is_even = False

# Check if the second number is even or odd
if second_number % 2 == 0:
    second_is_even = True
else:
    second_is_even = False

# Determine if the product will be even or odd based on the numbers' parity
if first_is_even or second_is_even:
    print(f"The product {first_number} x {second_number} will be an even number.")
else:
    print(f"The product {first_number} x {second_number} will be an odd number.")

