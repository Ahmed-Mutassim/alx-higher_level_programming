#!usr/bin/python3
"""prints the ASCII alphabet, in lowercase"""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
