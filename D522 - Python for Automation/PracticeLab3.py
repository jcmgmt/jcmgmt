"""

16.3 Practice Lab 3
A list of application logs have been collected. Each log's details are stored in a dictionary with the keys app, level, message, and timestamp. Updates to the log details are needed based on the following requirements:

Change the log level to "ERROR" for the log with application name webserver.
Update the timestamp to "2023-12-07T12:30:00" for the log with application name database.
Complete the Python function update_log_list. The function should accept a list of dictionaries representing log files, update the values in the log files based on the two requirements, and return the updated list of log files.

Only the update_log_list function will be graded for this assessment. The function should work for any list of dictionaries passted to update_log_list beyond the examples provided.

Example: If the stored log files are

log_sample = [
  {"app": "webserver", "level": "INFO", "message": "System error", "timestamp": "2023-12-07T12:25:00"},
  {"app": "database", "level": "WARN", "message": "High CPU usage", "timestamp": "2023-12-07T12:20:00"}]
the expected return is

[{'app': 'webserver', 'level': 'ERROR', 'message': 'System error', 'timestamp': '2023-12-07T12:25:00'}, {'app': 'database', 'level': 'WARN', 'message': 'High CPU usage', 'timestamp': '2023-12-07T12:30:00'}]
Example: If the stored log files are

log_sample = [
    {"app": "webserver", "level": "ERROR", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
    {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "2023-12-07T11:50:00"}]
the expected return is

[{'app': 'webserver', 'level': 'ERROR', 'message': 'Critical error', 'timestamp': '2023-12-07T11:55:00'}, {'app': 'database', 'level': 'ERROR', 'message': 'Database connection lost', 'timestamp': '2023-12-07T12:30:00'}]

"""

def update_log_list(log_list):
    for log in log_list:
        if log["app"] == "webserver":
            log["level"] = "ERROR"
        elif log["app"] == "database":
            log["timestamp"] = "2023-12-07T12:30:00"
    return log_list

# You may alter the code below to test your solution or print help documentation.
# Only the update_log_list function will be graded for this assessment.

log_sample = [
    {"app": "webserver", "level": "ERROR", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
    {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "2023-12-07T11:50:00"}]
#print(update_log_list(log_sample))
# help(help)

"""

Practice Lab 4: Updating Employee Records
A list of employee records has been collected. Each employee's details are stored in a dictionary with the keys name, role, salary, and last_promotion_date. Updates to the employee details are needed based on the following requirements:

Change the role to "Manager" for the employee with the name "Alice".
Update the last_promotion_date to "2024-01-01" for the employee with the name "Bob".
Complete the Python function update_employee_list. The function should accept a list of dictionaries representing employee records, update the values in the records based on the two requirements, and return the updated list of employee records.

Example: If the stored employee records are

python
Copy code
employee_sample = [
    {"name": "Alice", "role": "Engineer", "salary": 75000, "last_promotion_date": "2023-06-10"},
    {"name": "Bob", "role": "Technician", "salary": 55000, "last_promotion_date": "2023-05-20"}
]
the expected return is

python
Copy code
[
    {"name": "Alice", "role": "Manager", "salary": 75000, "last_promotion_date": "2023-06-10"},
    {"name": "Bob", "role": "Technician", "salary": 55000, "last_promotion_date": "2024-01-01"}
]


"""
def update_employee_list(records):
    for employee in records:
        if employee["name"] == "Alice":
            employee["role"] = "Manager"
        elif employee["name"] == "Bob":
            employee["last_promotion_date"] = "2024-01-01"
    return records

records = [
    {"name": "Alice", "role": "Engineer", "salary": "75000", "last_promotion_date": "2023-06-10"},
    {"name": "Bob", "role": "Technician", "salary": "55000", "last_promotion_date": "2023-05-20"}
]

#print(update_employee_list(records))
"""

Practice Lab 5: Modifying Order Details
A list of customer order details has been collected. Each order's details are stored in a dictionary with the keys order_id, customer_name, status, and total_amount. Updates to the order details are needed based on the following requirements:

Change the status to "Shipped" for the order with order_id 1002.
Update the total_amount to 125.50 for the order with order_id 1003.
Complete the Python function update_order_list. The function should accept a list of dictionaries representing customer orders, update the values in the orders based on the two requirements, and return the updated list of orders.

Example: If the stored orders are

python
Copy code
order_sample = [
    {"order_id": 1001, "customer_name": "John Doe", "status": "Pending", "total_amount": 75.00},
    {"order_id": 1002, "customer_name": "Jane Doe", "status": "Pending", "total_amount": 50.00},
    {"order_id": 1003, "customer_name": "Alice Smith", "status": "Processing", "total_amount": 100.00}
]
the expected return is

python
Copy code
[
    {"order_id": 1001, "customer_name": "John Doe", "status": "Pending", "total_amount": 75.00},
    {"order_id": 1002, "customer_name": "Jane Doe", "status": "Shipped", "total_amount": 50.00},
    {"order_id": 1003, "customer_name": "Alice Smith", "status": "Processing", "total_amount": 125.50}
]

"""

def update_order_list(order_sample):
    for order in order_sample:
        if order["order_id"] == 1002:
            order["status"] = "Shipped"
        elif order["order_id"] == 1003:
            order["total_amount"] = "125.50"
    return order_sample

order_sample = [
    {"order_id": 1001, "customer_name": "John Doe", "status": "Pending", "total_amount": 75.00},
    {"order_id": 1002, "customer_name": "Jane Doe", "status": "Pending", "total_amount": 50.00},
    {"order_id": 1003, "customer_name": "Alice Smith", "status": "Processing", "total_amount": "100.00"}
]

print(update_order_list(order_sample))