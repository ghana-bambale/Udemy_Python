parrot =   "Norwegian Blue"
# indexing  0123456789
#Learn indexing
# We can access the characters from the string but cant edit the string
# indexing starts at 0 for first character and goes on
# Task - Print "woBau" from string to output by accessing its index, each character on separate line

print(parrot[3])
print(parrot[1])
print(parrot[10])
print(parrot[7])
print(parrot[12])
print(5*'-')
# ----------------------------
# We can acheive the same goal by using negative indices for the characters in the string
# last character gets index -1, the one before that gets -2 and so on
# Print the same characters as above using negative indices
print(parrot[-11])
print(parrot[-13])
print(parrot[-4])
print(parrot[-7])
print(parrot[-2])
print(5*'-')
# -----------------
# The same can be achieved using the expression
# use the possitive index and subtract the length of string from it

print(parrot[3-14])
print(parrot[1-14])
print(parrot[10-14])
print(parrot[7-14])
print(parrot[12-14])
print(5*'-')
