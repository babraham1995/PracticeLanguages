# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def passwordGenerator(num):
    a = []
    for i in range(0, num):
        #generate random chars or words from api
        a.append(i)
    
    return "".join([str(x) for x in a])

print(passwordGenerator(8))



# list_string = map(str, list_int)

# output = [str(x) for x in list_string]