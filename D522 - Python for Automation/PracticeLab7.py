"""

16.7 Practice Lab 7
An existing function line_count is meant to open a text file, read the contents, and return the number of lines in the file. Several existing issues throw errors, and the function is not working as intended.

Update the code within the Python function line_count. The function should accept a string identifying the name of a text file, read the contents of the text file, determine the number of lines in the text file, and return the number of lines in the text file. For simplicity, assume each line except the last ends with a newline character.

Only the line_count function will be graded for this assessment. The function should work for any text file passed to line_count beyond the examples provided.

Example: If the text file "test.txt" contains

Line 1
Line 2
Line 3
the expected return is

3
Example: If the text file "lorem.txt" contains

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque tincidunt velit non iaculis porttitor.
Phasellus mattis, metus non posuere mollis, eros augue dictum.
Quisque porttitor est nec eros maximus, id sodales.
the expected return is

4

"""

# Modify this function.
def line_count(filename):
    f = open(filename,'r') 
    contents = f.readlines()
    lines = contents.split("\n")
    f.close()
    return len(lines)


# You may alter the code below to test your solution or print help documentation.
# Only the line_count function will be graded for this assessment.

print(line_count('test.txt'))
# help(help)
file = open("Test.txt", 'r')
list = file.readlines()
#lines = list.split("\n")
print(len(list))
"""

An existing function word_count is meant to open a text file, read the contents, and return the number of words in the file. However, several issues throw errors, and the function is not working as intended.

Update the code within the Python function word_count. The function should accept a string identifying the name of a text file, read the contents of the text file, count the total number of words, and return the word count. For simplicity, assume words are separated by spaces.

Example: If the text file "test.txt" contains:

bash
Copy code
Hello world
This is a test
the expected return is:

Copy code
5
If the text file "lorem.txt" contains:

Copy code
Lorem ipsum dolor sit amet
consectetur adipiscing elit
the expected return is:

Copy code
6


"""

#ENTER CODE

"""

An existing function char_count is intended to open a text file, read the contents, and return the number of characters in the file (including spaces). However, the function has errors and is not functioning properly.

Update the code within the Python function char_count. The function should accept a string identifying the name of a text file, read the contents of the text file, count the total number of characters (including spaces and newline characters), and return the character count.

Example: If the text file "test.txt" contains:

Copy code
Hello
World
the expected return is:

Copy code
11
(There are 10 characters and 1 newline character between the words.)

If the text file "lorem.txt" contains:

Copy code
Lorem ipsum
dolor sit amet
the expected return is:

Copy code
22


"""

#ENTER CODE