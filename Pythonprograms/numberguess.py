# program for guessing the number in the game
import random
number = random.randrange(1,10)
guess = int(input("Enter any number(1-10):"))
while number!=guess:
    if guess < number:
        print("Too Low")
        guess = int(input("Enter the number again:"))
    elif guess > number:
        print("Too high")
        guess = int(input("Enter the number again:"))
    else:
        break
print("You Guessed the right number !!")

