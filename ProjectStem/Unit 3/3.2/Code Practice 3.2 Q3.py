"""
Test if a password entered is correct. The secret phrase is “Amedeo Avogadro” (without the quotes).
Sample Run 1

Enter the password: Amedeo Avogadro

Sample Output 1

Correct!

Sample Run 2

Enter the password: Georg Cantor

Sample Output 2

Not Correct

"""

name = input("Enter the password: ")
if name == "Amedeo Avogadro":
    print("Correct!")
else:
   print("Not Correct")