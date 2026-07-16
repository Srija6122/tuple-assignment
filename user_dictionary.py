# Empty dictionary
users = {}

# Add user
def add_user(user_id, name):
    users[user_id] = name
    print("User added:", users)

# Get user
def get_user(user_id):
    if user_id in users:
        print("User Name:", users[user_id])
    else:
        print("User ID not found")

# Update user
def update_user(user_id, new_name):
    if user_id in users:
        users[user_id] = new_name
        print("Updated:", users)
    else:
        print("User ID not found")

# Remove user
def remove_user(user_id):
    if user_id in users:
        del users[user_id]
        print("After removing:", users)
    else:
        print("User ID not found")

# Test functions
add_user(101, "Srija")
add_user(102, "Rahul")

get_user(101)

update_user(102, "Kiran")

remove_user(101)