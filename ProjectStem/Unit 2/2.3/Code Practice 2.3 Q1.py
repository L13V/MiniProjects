"""
Write a program that prompts the user to input two POSITIVE numbers — a dividend (numerator) and a divisor (denominator).  Your program should then divide the numerator by the denominator. Lastly, your program will add the quotient and the remainder together.

Sample Run:

Input the dividend: 10
Input the divisor: 4
The quotient + the remainder is 4.0

Hint: If you use division (/) to calculate the quotient, you will need to use int() to remove the decimals. You can also use integer division (// ), which was introduced in Question 5 of Lesson Practice 2.3.

Once you've calculated the quotient, you will need to use modular division (%) to calculate the remainder. Remember to clearly define the data types for all inputs in your code. You may need to use int( ) and str( ) in your solution.

int( ): When you divide the numerator and the divisor using /, make sure that the result is an integer.

str( ): After using modular division, you can transform the quotient and remainder back into strings to display the result in the print() command.
"""

dividend = int(input("Input the dividend: "))
divisor = int(input("Input the divisor: "))
quotient = dividend // divisor
mod = dividend % divisor
print("The quotient + the remainder is " + str(quotient + mod))
