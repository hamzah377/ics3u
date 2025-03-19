import random

a = random.randrange(1,100) 
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")
c = 1 
x = 0
while c < 7 and x != a:
    x = int(input("Guess #" + str(c) + ": "))
    if x < a:
       print("Higher")
    if x > a:
       print("Lower")
    if x == a:
       print("You Guessed right!")
    c += 1
if c >= 7 and x != a:
    print("you are out of guesses! The answer was" , a , ". Better luck next time!")
