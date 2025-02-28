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
