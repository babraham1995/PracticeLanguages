# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 2, 3, 3, 4, 1, 1, 5, 6, 6, 7, 1]
b=[]

#answer as a loop 
   
def easyModeVersion(a):
  y = []
  for i in a:
    if i not in y:
      y.append(i)
  print('easymode: ', y)
  return y

easyModeVersion(a)

def duplicateLoop(i):
    for x in range(0, len(a)):
        if x==i:
            break
        if a[i]==a[x]:
            return
    b.append(a[i])


for i in range(0, len(a)):
    duplicateLoop(i)
print('duplicatesRemovedList: ', b)

#answer as a set

bruh = list(dict.fromkeys(a))
print("duplicatesRemovedList2:", bruh)
