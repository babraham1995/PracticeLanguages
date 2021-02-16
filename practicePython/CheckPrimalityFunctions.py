# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below

input1 = int(input("input a number: "))

"""
 for x in range (2, number - 1):
     should count up from 0 for more efficiency
"""

for i in range(input1-1, 1, -1):
    if input1%i==0:
        print("not prime")
        break
else: print("it's prime")
   
