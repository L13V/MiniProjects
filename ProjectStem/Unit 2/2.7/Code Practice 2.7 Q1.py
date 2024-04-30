"""
Write a program that takes three numbers as input from the user, and prints the smallest.

Hint: Remember that the numbers should be compared numerically. Any input from the user must be transformed into an integer, but printed as a string.
Sample Run

Enter a number: 20
Enter a number: 50
Enter a number: 5

Smallest: 5

"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

print("Smallest: " + str(min(num1, num2, num3)))