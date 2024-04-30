"""
Currently, this program will add 6 and 3 together, output the math problem and output the answer. Edit this code so that a random number is generated from 1 - 5 (inclusive) for the variables a and b. Also, instead of adding the two numbers together, the edited program should multiply them, and output the proper math problem and answer. Be sure to update every line of code to reflect the changes needed.
"""
import random

a = random.randint(1, 5)
b = random.randint(1, 5)

answer = a * b

print (str(a) + " * " + str(b) + " = " + str(answer)) 
