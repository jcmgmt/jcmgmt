"""16.5 Practice Lab 5
A Python function same_subnetconverts IP addresses and subnet mask to binary strings in order to determine if two IPv4 addresses are in the same subnet, returning a string indicating whether both IP addresses are in the same subnet or not.

Complete the Python function same_subnet. The function should accept three strings representing two IP addresses and a subnet mask, determine if both IP addresses are in the same subnet, and return a predefined string statement indicating if both IP addresses are in the same subnet.

Only the same_subnet function will be graded for this assessment. The function should work for any IP addresses or subnet masks passed to same_subnet beyond the examples provided.

Example: If the two IP addresses and subnet mask are

'192.168.1.100', '192.168.1.200', '255.255.255.0'
the expected return is

192.168.1.100 and 192.168.1.200 are in the same subnet
Example: If the two IP addresses and subnet mask are

'192.168.1.100', '192.168.2.200', '255.255.255.0'
the expected return is

192.168.1.100 and 192.168.2.200 are not in the same subnet
"""

def same_subnet(ip1, ip2, subnet_mask):
    # convert IP addresses to binary strings
    ip1_bin = ''.join([format(int(x), '08b') for x in ip1.split('.')])
    ip2_bin = ''.join([format(int(x), '08b') for x in ip2.split('.')])

    # convert subnet mask to binary string
    subnet_bin = ''.join([format(int(x), '08b') for x in subnet_mask.split('.')])

    # get network address portion for both IP addresses
    subnet_len = subnet_bin.count('1')
    network1_bin = ip1_bin[:subnet_len]
    network2_bin = ip2_bin[:subnet_len]

    # Predefined statement indicating if IP addresses are in the same subnet
    x = f"{ip1} and {ip2} are in the same subnet"
    y = f"{ip1} and {ip2} are not in the same subnet"
    
    # Write a conditional expression to check if both IP addresses are in the same subnet
    # and return the appropriate string output x or y.
    # Write your code here.
    if network1_bin == network2_bin:
        return x
    else:
        return y


# You may alter the code below to test your solution or print help documentation.
# Only the same_subnet function will be graded for this assessment.

print(same_subnet('192.168.1.100', '192.168.1.200', '255.255.255.0'))