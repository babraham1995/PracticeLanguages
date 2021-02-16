from random import random
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# input1 = int(input("guess the number between 1 to 9: "))

# seed(1)
number = int(random()*8+1)
print(number)

while True:
    input1 = int(input("guess the number between 1 to 9: "))
    if input1>9:
        print("guess too high")
    elif input1-number>0:
        print("too high")
    elif input1-number<0:
        print("too low")
    elif input1==number:
        print("nice one")
        break