"""
Test if a number grade is an F (less than or equal to 65). If so, print "That's not good.".

Hint: Grades may be decimals.
Sample Run

Enter a Number: 60

Sample Output

That's not good.

"""

num = input("Enter a Number: ")

if float(num) <= 65:
    print("That's not good.")   