"""
16.10 Practice Lab 10
A bug has been submitted for a Python function named scan_ports. The function is supposed to use the socket library to scan the loopback address and check if ports 0-x are open/closed and return a list of tuples with the port status. Correct the logical errors in the code.

Here is an example of the usage:

 print(scan_ports(5))
Here is an example of the expected output:

[(0, 'OPEN'), (1, 'OPEN'), (2, 'OPEN'), (3, 'OPEN'), (4, 'OPEN'), (5, 'OPEN')]
The Zybooks coding environment lacks outside connectivity, code to mock the return value for socket.connect_ex has been provided to allow normal use of the socket library for the socket.connect_ex function only. socket.connect_ex should always return 0 for this assessment.
"""
import socket
import time
import unittest.mock as mock

def scan_ports(x):
    # Mock socket
    with mock.patch('socket.socket') as mock_socket:
        mock_socket.return_value.connect_ex.return_value = 0 # do not edit
        target_IP = '127.0.0.1'

        # Instantiate a socket object.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the socket operations.
        s.settimeout(5)  

        # Create an empty list to store port status as a list tuples.
        open_ports = []  

        # Iterate over ports checking the connection and appending the port status to the list.
        for i in range(0, x+1):
            conn = s.connect_ex((target_IP, i))
            if(conn == 0):
                open_ports.extend(open_ports + [i, 'CLOSED'])
            else:
                open_ports.extend(open_ports + [i, 'OPEN'])

        # Close the socket connection.
        s.close()

        # Return the list of open ports as a list of tuples.
        return open_ports

# You may alter the code below to test your solution or print help documentation.
# Only the scan_ports function will be graded for this assessment.

# print(scan_ports(5))
# help(socket.socket)
# help(socket.socket.connect_ex)