print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

# Part 1: Even or Odd Multiplication
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

if (num1 % 2 == 0) or (num2 % 2 == 0):
    print("The product", num1, "x", num2, "will be an even number.")
else:
    print("The product", num1, "x", num2, "will be an odd number.")

# Part 2: Cube Body Diagonal Calculation
print("\nI will find the cube's inner diagonal for any edge length!")
edge_length = float(input("Please enter the edge length of your cube: "))
diagonal = (edge_length * (3 ** 0.5))
print("The length of the inner diagonal of a cube with side length", edge_length, "is:", round(diagonal, 2))

# Part 3: Making Change in Coins
print("\nCoin Change Calculator (amounts less than $1.00)")
cents = int(input("Please enter the amount of change in cents: "))

# Ensure the amount is less than a dollar
cents = cents % 100  # If user enters more than 100 cents, subtract the extra dollars

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

# Print results
print("Change given:", end=" ")
if quarters > 0:
    print(quarters, "quarter" + ("s" if quarters > 1 else ""), end="")
if dimes > 0:
    print(",", dimes, "dime" + ("s" if dimes > 1 else ""), end="")
if nickels > 0:
    print(",", nickels, "nickel", end="")
if pennies > 0:
    print(",", pennies, "penn" + ("ies" if pennies > 1 else "y"), end="")
print(".")
