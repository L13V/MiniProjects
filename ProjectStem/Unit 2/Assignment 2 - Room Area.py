"""
https://files.projectstem.org/CSFundamentals/CSF_Images/U2_A2_Lab_image.png
For this lab, you will find the area of an irregularly shaped room with the shape as shown above.

Ask the user to enter the values for sides A, B, C, D, and E and print out the total room area.

Remember the formula for finding the area of a rectangle is length * width and the area of a right triangle is 0.5 * the base * height.

Please note the final area should be in decimal format.
Sample Run

Enter side A: 11
Enter side B: 2
Enter side C: 4
Enter side D: 7
Enter side E: 1

Sample Output

Room Area: 53.5
"""

# User Input

sidea = int(input("Enter side A: "))
sideb = int(input("Enter side B: "))
sidec = int(input("Enter side C: "))
sided = int(input("Enter side D: "))
sidee = int(input("Enter side E: "))

print("Room Area: " + str((sidea * sideb) + ((sidea - sidec) * (sided - sidee - sideb)) + ((sidee * (sidea - sidec) / 2))))

# Calculates Main square's area, adds the smaller secondary square's (to the right) area to the total, and then calculated the sides for the triangle, then divides it by 2