"""
Write a program that inputs the length of two pieces of wood in yards and feet (as whole numbers) and prints the total.
Sample Run

Enter the Yards: 3
Enter the Feet: 2
Enter the Yards: 4
Enter the Feet: 1

Sample Output

Yards: 8 Feet: 0

Hint: Change all of the inputs into feet first - remember there are 3 feet in each yard. Now that the wood is in feet, find the yards and feet similarly to the last practice, using regular and modular division.
"""

#Note: This can be SERIOUSLY condensed. I have made the most readable code possible, but almost ALL the calculations can be put in one-liners.

# Take User Input

yard1 = int(input("Enter the Yards: "))
ft1 = int(input("Enter the Feet: "))
yard2 = int(input("Enter the Yards: "))
ft2 = int(input("Enter the Feet: "))

# Convert all to feet

yard1nFeet = int(yard1 * 3)
yard2nFeet = int(yard2 * 3)

# Calculate total in feet

totalfeet = yard1nFeet + yard2nFeet + ft1 + ft2

# Calculate total whole yards

totalwholeyards = int(totalfeet // 3)
ftRemainder = int(totalfeet % 3)

print("Yards: " + str(totalwholeyards) + " Feet: " + str(ftRemainder))