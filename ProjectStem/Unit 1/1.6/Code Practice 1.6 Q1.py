"""
Write a program that uses two input statements to get two words as input. Then, print the words on one line separated by a space. Your program's output should only include the two words and a space between them.
Hint: To print both words on one line, remember that you can concatenate (add) two phrases by using the + symbol.  Don't forget that you'll need to add a space between the words as well.

Sample Run:
Enter a word: Hello
Enter a word: World
Hello World
"""

word1Inp = input("Enter a word")
word2Inp = input("Enter a word")
print(word1Inp + " " + word2Inp)