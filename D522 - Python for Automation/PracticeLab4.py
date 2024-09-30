"""

16.4 Practice Lab 4
A business requires that each employee ID begins with a department identifier and ends with an individual identifier (e.g., "HRD00123", "ENG00567"). The department identifier is a 3-letter department code in all uppercase. The individual identifier is a 5-digit numeric value.

Complete the Python script to create a custom function name validate_id. The function should accept a string parameter representing an employee ID, determine if the ID meets the requirements, and return a Boolean value, with True returned if all requirements are met and False returned if any requirement is not met.

Only the validate_id function will be graded for this assessment. The function should work for any string representing an ID passed to validate_id beyond the examples provided.

Example: If the string representing an employee ID is

HRD00123
the expected return is

True
Example: If the string representing an employee ID is

Ops123456
the expected return is

False

"""

def validate_id(insertid):
    insertid = insertid.upper()
    if len(insertid) == 8 and insertid[:3].isalpha() and insertid[3:].isdigit():
        #if insertid[-3:]
        return True
    else:
        return False


# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.
#insertid = "HRD00123"
#print(len(insertid))
#print(validate_id("HRD00123"))
# help(help)

"""

A company requires that each product code starts with a 4-letter uppercase category identifier and ends with a 6-digit numeric value (e.g., "ELEC000123", "FURN001234"). The category identifier is exactly 4 uppercase letters, and the numeric value is exactly 6 digits.

Complete the Python script to create a custom function validate_product_code. The function should accept a string parameter representing a product code, determine if the code meets the requirements, and return a Boolean value, with True returned if all requirements are met and False returned if any requirement is not met.

Example: If the string representing a product code is

python
Copy code
ELEC000123
the expected return is

python
Copy code
True
If the string representing a product code is

python
Copy code
Elec12345
the expected return is

python
Copy code
False


"""
def validate_product_code(insertcode):
    insertcode = insertcode.upper()
    if len(insertcode) == 10 and insertcode[:4].isalpha() and insertcode[4:].isdigit():
        return True
    else:
        return False
    
# print(validate_product_code("Elec123452"))

"""

A regional transportation department requires that each vehicle license plate consists of two uppercase letters followed by four digits (e.g., "AB1234", "XY5678"). The letters represent the region, and the digits represent the vehicle number.

Complete the Python script to create a custom function validate_license_plate. The function should accept a string parameter representing a license plate, determine if it meets the format requirements, and return a Boolean value, with True returned if the plate meets the format and False if it does not.

Example: If the string representing a license plate is

python
Copy code
AB1234
the expected return is

python
Copy code
True
If the string representing a license plate is

python
Copy code
A12345
the expected return is

python
Copy code
False


"""

def validate_license_plate(licenseplate):
    licenseplate = licenseplate.upper()
    if len(licenseplate) == 6 and licenseplate[:2].isalpha() and licenseplate[2:].isdigit():
        return True
    else:
        return False
    
print(validate_license_plate("AB1111"))