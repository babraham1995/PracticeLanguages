# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock


input1 = int(input("player one you're up: "))
input2 = input("player two you're up: ")


# options[input1]


def RockandRock():
    print("Tie.\n")

# def RockandPaper():
#     print "n is a perfect square\n"

# def RockandScissor():
#     print "n is an even number\n"

# def PaperandRock():
#     print "n is a prime number\n"

# def PaperandPaper():
#     print "Tie.\n"

# def PaperandScissor():
#     print "n is a prime number\n"

# def ScissorandRock():
#     print "n is a prime number\n"

# def ScissorandPaper():
# print "n is a prime number\n"

# def ScissorandScissor():
# print "Tie.\n"

# map the inputs to the function blocks
options = {0 : RockandRock,
        #    1 : sqr,
        #    4 : sqr,
        #    9 : sqr,
        #    2 : even,
        #    3 : prime,
        #    5 : prime,
        #    7 : prime,
}

options[input1]

print('hi', options[0])