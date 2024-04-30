"""
Write the code to input a number and calculate the square root. Use the absolute value function to make sure that if the user enters a negative number, the program does not crash. Lastly, write a print statement that states "The final outcome is " followed by the square root and remember to change the final outcome to a string.
Sample Run

Enter a number: -16
The final outcome is: 4.0

"""
import math

num = int(input("Enter a number: "))
print("The final outcome is: " + str(math.sqrt(math.fabs(num))))
