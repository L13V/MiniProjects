
"""
In your Code Editor, there is some code meant to output verses of the song "Old MacDonald had a farm."

When the code is working properly, if the user types in pig for an animal (when prompted to "Enter an animal: ") and oink for the sound (when prompted to "Enter a sound: "), the program should output the following as it runs:

Old Macdonald had a farm, E-I-E-I-O
And on his farm he had a pig, E-I-E-I-O
With a oink-oink here and a oink-oink there
Here a oink there a oink
Everywhere a oink-oink
Old Macdonald had a farm, E-I-E-I-O

There are a few errors in the code provided in the Code Editor. Your task is to debug the code so that it outputs the verses correctly.

Hints:

    Try running the code and looking closely at what is output.  The output can be a clue as to where you will need to make changes in the code you are trying to debug.
    Check the variable assignments carefully to make sure that each variable is called correctly.
    Look at the spacing at the end of strings - does each string have the appropriate number of spaces after it?
"""

animal = input("Enter an animal: ")
sound = input("Enter a sound: ")

e = "E-I-E-I-O"

print("Old Macdonald had a farm, " + e)
print("And on his farm he had a " + animal + ", " + e)
print("With a " + sound + "-" + sound + " here and a " + sound + "-" + sound + " there")
print("Here a "+ sound + " there a " +sound)
print("Everywhere a " + sound + "-" + sound)
print("Old Macdonald had a farm, " + e)