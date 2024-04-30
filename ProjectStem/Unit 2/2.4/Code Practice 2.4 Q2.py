"""
Write a program that accepts a number as input, and prints just the decimal portion. Your program should also work if a negative number is inputted by the user. Lastly, write a print statement that states “The final outcome is: ”, followed by the decimal portion, and remember to change the final outcome to a string.
Sample Run

Enter a number: 15.789

Sample Output

The final outcome is: 0.789

"""

import math

num = float((input("Enter a number: ")))
print("The final outcome is: " + str(math.fabs(num) % 1))
