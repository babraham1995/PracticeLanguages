number = int(input("Enter a Number: "))
output = number/2

# solution 1
if number%4==0:
    print("excuse me there bruh, you seem to have a multiple of 4")
    exit()
if number%2 == 0: 
    print("Bruh thats even", number%2)
if number%2 != 0:
    print("Bruh thats odd", number%2)

# solution 2
while True: 
    if number%4==0:
        print("excuse me there bruh, you seem to have a multiple of 4")
        break
    if number%2 == 0: 
        print("Bruh thats even", number%2)
        break
    if number%2 != 0:
        print("Bruh thats odd", number%2)
        break

#solution 3

def my_function(n):
    while True: 
        if n==1:
            print("excuse me there bruh, you seem to have a multiple of 4")
            break
        if n==2: 
            print("Bruh thats even", number%2)
            break
        if n==3:
            print("Bruh thats odd", number%2)
            break

if number%4==0:
    my_function(1)
    exit()
if number%2 == 0: 
    my_function(2)
    exit()
if number%2 != 0:
    exit()
    my_function(3)      