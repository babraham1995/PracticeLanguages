# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# Discussion

# Concepts for this week:

# List indexing
# Strings are lists

# print("brocation"[3::+1])
# print("1")
# print("brocation"[:3:+2])
# print("2")
# print("brocation"[3::-1])
# print("brocation"[:3:-1])
# print("brocation"[3:-1])
# print("3")
# print("brocation"[:7:-1])
# print("4")
# print("brocation"[:3:-1])
# print("5")
# print("brocation"[:3:-1])
# print("6")
# print("brocation"[:5:-1])

input = input("enter palindrome: ")

backwardsWord = input[::-1] 

print(input[1:2:-1])

if input == backwardsWord:
    print("its a palindrome")
else: print("nah its not bro")