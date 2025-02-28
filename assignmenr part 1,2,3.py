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
    Part 2: The inner (or body) diagonal of a cube
import math

def calculate_cube_diagonal(edge_length):
    # Formula for the body diagonal of a cube
    diagonal = math.sqrt(3) * edge_length
    # Round the result to 2 decimal places
    return round(diagonal, 2)

def main():
    print("I will find the cube's inner diagonal for any edge length!")
    edge_length = float(input("Please enter the edge length of your cube: "))
    diagonal = calculate_cube_diagonal(edge_length)
    print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {diagonal}")

if __name__ == "__main__":
    main()

Part 3: Making change in coins
# Main program to make change for amounts less than $1.00 using the fewest coins
print("Welcome to the Change Maker Program!")

# Get the amount of change from the user
amount = int(input("Please enter the amount of change in cents: "))

# If the amount is 100 cents or more, subtract the dollar value
if amount >= 100:
    amount = amount % 100  # Keep only the cents remaining after subtracting full dollars

# Initialize coin variables
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# Calculate the number of quarters
if amount >= 25:
    quarters = amount // 25
    amount = amount % 25  # Update the remaining amount after using quarters

# Calculate the number of dimes
if amount >= 10:
    dimes = amount // 10
    amount = amount % 10  # Update the remaining amount after using dimes

# Calculate the number of nickels
if amount >= 5:
    nickels = amount // 5
    amount = amount % 5  # Update the remaining amount after using nickels

# The remaining amount is all pennies
pennies = amount  # The rest of the amount will be pennies

# Build the result message
result = str(quarters * 25 + dimes * 10 + nickels * 5 + pennies) + " cents can be "

# Add coins to the result string
if quarters > 0:
    result += str(quarters) + " quarter" + ("s" if quarters > 1 else "") + ", "
if dimes > 0:
    result += str(dimes) + " dime" + ("s" if dimes > 1 else "") + ", "
if nickels > 0:
    result += str(nickels) + " nickel" + ("s" if nickels > 1 else "") + ", "
if pennies > 0:
    result += str(pennies) + " penny" + ("ies" if pennies > 1 else "")

# Remove the last comma and space
result = result.rstrip(", ")

# Print the result
print(result + ".")


