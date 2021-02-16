# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

b = "bernie is my name"

def reverseString(b):
    a = []
    c = b.split(" ")

    for i in c[::-1]:
        a.append(i)

    return a


result = " ".join(reverseString(b))
print(result)

#one liner

def reverseWord(w):
  return ' '.join(w.split(" ")[::-1])

print(reverseWord(b))