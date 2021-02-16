#return if its odd or even in a one liner 

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#my solution, redundant logic at start
b = [i*(i%2) for i in a if i%2!=0]
#site solution
b = [number for number in a if number % 2 == 0]

print(b)


#   years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
#   ages = []
#   for year in years_of_birth: 
#     ages.append(2014 - year)
# And at the end, the variable ages has the list [24, 23, 24, 24, 22, 23]. What this code did was translate the years of birth into ages, and it took us a for loop and an append statement to a new list to do that.

# Compare to this piece of code:

#   years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
#   ages = [2014 - year for year in years_of_birth]