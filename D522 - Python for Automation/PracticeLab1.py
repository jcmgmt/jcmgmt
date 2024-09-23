"""

16.1 Practice Lab 1
An outdated design file has stored red, blue, and green (RGB) color values as separate integer values within a list. Combine all three color values into a single string value properly formatted as an RGB color.

Complete the Python function format_rgb. The function should accept a list of integers representing separate RGB values, combine the RGB values into a single string value properly formatted as an RGB color, and return the formatted RGB color. A formatted RGB color does not contain space characters between values.

Only the format_rgb function will be graded for this assessment. The function should work for any list of integers passed to format_rgb beyond the examples provided.

Example: If the stored RGB values are

[255, 165, 13]
the expected return is

rgb(255,165,13)
Example: If the stored RGB values are

[0, 0, 0]
the expected return is

rgb(0,0,0)

"""

def format_rgb(rgb):
    r, g, b = rgb
    return f"rgb({r},{g},{b})"
    return rgb


# You may alter the code below to test your solution or print help documentation.
# Only the format_rgb function will be graded for this assessment.

rgb_sample = [255, 165, 13]
print(format_rgb(rgb_sample))
# help(help)