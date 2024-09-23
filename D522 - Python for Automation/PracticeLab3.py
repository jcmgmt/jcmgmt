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
# print(update_log_list(log_sample))
# help(help)