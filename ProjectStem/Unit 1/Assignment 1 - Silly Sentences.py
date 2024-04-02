"""
Write a program that will ask the user for a series of words. Then plug them into our paragraph template.

Be careful! The order in which you ask the user for the words matters and needs to match the sample run below. 
Sample Run

Let's play Silly Sentences!

Enter a name: Grace
Enter an adjective: stinky
Enter an adjective: blue
Enter an adverb: quietly
Enter a food: soup
Enter another food: bananas
Enter a noun: button
Enter a place: Paris
Enter a verb: jump

Grace was planning a dream vacation to Paris.
Grace was especially looking forward to trying the local
cuisine, including stinky soup and bananas.

Grace will have to practice the language quietly to
make it easier to jump with people.

Grace has a long list of sights to see, including the
button museum and the blue park.

Output Template

Your output should be based on this template:

Let's play Silly Sentences!

[name] was planning a dream vacation to [place].
[name] was especially looking forward to trying the local
cuisine, including [adjective 1] [food 1] and [food 2].
 
[name] will have to practice the language [adverb] to
make it easier to [verb] with people.
 
[name] has a long list of sights to see, including the
[noun] museum and the [adjective 2] park.

Benchmarks

As you work on Assignment 1, you may find it helpful to track your progress against the benchmarks listed below.  Follow the steps in order to ensure that you are writing clear, concise code that will meet all criteria.  Remember that the formatting of your output must be exact - be careful about the spacing and line breaks.

    Using the print() function, output, "Let's play Silly Sentences!"  
    Using the input() function, prompt the user to, "Enter a name: ", then assign and store their response to a variable.
    Repeat benchmark 2 for the other 8 inputs that we need from the user: adjective, adjective, adverb, food, food, noun, place, and verb.
    Using a print() function, output, "[name] was planning a dream vacation to [place]." Replace [name] and [place] with the proper variables.
    Repeat step 4 with the other 6 lines of output.
    Double-check to make sure the output is formatted correctly - including spaces before and after variables and line spacing.
    Run and test your program with the values from the Sample Run.
    Debug and repeat step 7 as needed.

Hint: Be careful of spaces and typos in your output.
"""


print("Let's play Silly Sentences!" + "\n") #Title, skips line for questions

#Questions, setting vars for print commands

name1 = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter an adjective: ")
adv1 = input("Enter an adverb: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")
noun1 = input("Enter a noun: ")
place1 = input("Enter a place: ")
verb1 = input("Enter a verb: ")

#Print code

print("\n" + name1 + " was planning a dream vacation to " + place1 + ".") #New line and first group of print code

print(name1 + " was especially looking forward to trying the local cuisine, including " + adj1 + " " + food1 + " and " + food2 + ".")

#2nd print code

print("\n" + name1 + " will have to practice the language " + adv1 + " to make it easier to " + verb1 + " with people.")

#3rd print code

print("\n" + name1 + " has a long list of sights to see, including the " + noun1 + " museum and the " + adj2 + " park.")