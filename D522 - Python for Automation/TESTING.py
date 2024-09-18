def generate_users(username_string, num_accounts):
    user = str(username_string)
    num = int(num_accounts)
    set1 = set()  # Use set instead of dict
    for i in range(1, num + 1):
        set1.add(f"{user}{i}")  # Add usernames to the set
    return set1  # Return the set of usernames

# Test the function
print(generate_users("test_account", 5))
