
"""
Write a program that asks the user to input the first and last names of a friend. The first prompt should state:

Please input your friend's first name: 

The second prompt should state:

Please input your friend's last name: 

After accepting the inputs, your program should output the input in the form last name, first name.

Hint: Remember that you can concatenate (add) two phrases by using the + symbol.  Don't forget that you'll need to add a comma as well and that the comma must be followed by a space.
"""

firstName = input("Please input your friend's first name:")
lastName = input("Please input your friend's last name:")
print(lastName + ", " + firstName)