"""
16.6 Practice Lab 6
A list of float values measuring the percentage of CPU usage for servers has been collected. Servers with CPU usage greater than 90% should be flagged.

Complete the Python function identify_high_cpu. The function should accept a list of floats representing the percentage of CPU usage for servers, determine which servers have higher than 90% CPU usage, and return the list of high-usage servers by index value.

Only the identify_high_cpu function will be graded for this assessment. The function should work for any list of floats passed to identify_high_cpu beyond the examples provided.

Example: If the stored CPU percentages are

[85.0, 92.5, 88.0, 95.2]
the expected return is

[1, 3]
Example: If the stored CPU percentages are

[91.0, 88.8, 89.5]
the expected return is

[0]

"""

def identify_high_cpu(cpu_list):
    highcpu = []
    for i, server in enumerate(cpu_list):
        if server > 90:
            highcpu.append(i)
    return highcpu
# You may alter the code below to test your solution or print help documentation.
# Only the identify_high_cpu function will be graded for this assessment.

cpu_list = [85.0, 92.5, 88.0, 95.2]
print(identify_high_cpu(cpu_list))
# help(help)