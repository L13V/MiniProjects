"""
Write a program to enter a decimal number and test if it is less than 26.4. If the number entered is less than 26.4, the program needs to output the phrase Less than 26.4..
Sample Run

Enter a number: 20.34

Sample Output

Less than 26.4

"""

num = input("Enter a number: ")
if float(num) < 26.4:
    print("Less than 26.4")