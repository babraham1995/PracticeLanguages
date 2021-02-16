input = int(input("please enter a number:"))

a = []
i = input
for i in range(input, 0, -1):
    if input%i ==0 :
        a.append(i)

print(a)



# Create a program that asks the user
#  for a number and then prints out a
#  list of all the divisors of that number. 
#  if you dont know what a divisor is
#  a number that divides evenly into another number.
#  For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

# age = int(input("How old are you: "))