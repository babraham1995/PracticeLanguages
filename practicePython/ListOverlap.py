import random
#Generate 5 random numbers between 10 and 30
a = random.sample(range(10, 30), 5)
b = random.sample(range(10, 30), 5)

print(a,b)

# a = [1,3,3]
# b=[1,2,3]
c=[]
d=[]

for i in range(len(a)):
    if a[i] == b[i]:
        c.append(a[i])

for i in range(len(a)):
    for x in range(len(b)):
        if a[i] == b[x]:
            d.append(a[i])

e = list(set(a).intersection(b))
commonalities = set(a) - (set(a) - set(b))

print(c)
print(d)
print(e)
print(commonalities)


# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# r