import random

a = random.randint(1, 100)
print("Guess the number (1-100)! You have 6 tries.")

for c in range(6):
    x = int(input("Your guess: "))
    if x == a:
        print("Correct! ")
        
    print("Higher" if x < a else "Lower")
else:
    print(f"Out of tries! The number was {a}.")
