# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock


input1 = int(input("rock:1, paper: 2, scissors: 3, player one you're up: "))
input2 = int(input("rock:1, paper: 2, scissors: 3: player two you're up: "))
winner = 0


# options[input1]


# if (input1 == 1) : 
#     if (input2 == 1):
#         print("Draw")
#     elif input2 == 2:
#         print("player two wins") 
#     elif input2 == 3:
#         print("player one wins")
# elif (input1 == 2) : 
#     if input2 == 1:
#         print("player two wins")
#     elif input2 == 2:
#         print("Draw") 
#     elif input2 == 3:
#         print("player one wins")
# elif (input1 == 3) : 
#     if input2 == 1:
#         print("player two wins")
#     elif input2 == 2:
#         print("player one wins") 
#     elif input2 == 3:
#         print("Draw")

# print("finished")

while True:
    if (input1 == 1) : 
        if (input2 == 1):
            winner = 0
            break
        elif input2 == 2:
            winner = 2
            break
        elif input2 == 3:
            winner = 1
            break
    elif (input1 == 2) : 
        if input2 == 1:
            winner = 2
            break
        elif input2 == 2:
            winner = 0
            break
        elif input2 == 3:
            winner = 1
            break
    elif (input1 == 3) : 
        if input2 == 1:
           winner = 1
           break
        elif input2 == 2:
            winner = 2
            break
        elif input2 == 3:
            winner = 0
            break
    else: 
        print("wrong input")
        exit()

print("finished, winner is: ", winner)









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

options[0]()

print('hi')
