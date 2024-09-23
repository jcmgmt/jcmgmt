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
    f = Open(filename) 
    contents = f.read
    lines = contents.split("\n")
    f.close()
    return len(line)

# You may alter the code below to test your solution or print help documentation.
# Only the line_count function will be graded for this assessment.

# print(line_count('test.txt'))
# help(help)