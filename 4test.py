from pip._vendor.distlib.compat import raw_input
print("Enter a character")
character = raw_input("--> ")
character = character[0]

if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
    print ("Input character is a Vowel.")
else:
    print ("Input character is a Consonant.")