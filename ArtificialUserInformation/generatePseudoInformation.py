import csv
import hashlib

# Number of users to generate
num_users = 700

# File paths for the generated CSVs
users_file = "Users.csv"
passwords_file = "UserPasswords.csv"

# Generate Users.csv
with open(users_file, mode="w", newline="") as users_csv:
    writer = csv.writer(users_csv)
    # Write header
    writer.writerow(["userId", "userName", "emailAddress", "userRole"])
    # Generate rows
    for user_id in range(1, num_users + 1):
        username = f"Anonymous{user_id}"
        email = f"{username}@example.com"
        role = "normal"
        writer.writerow([user_id, username, email, role])

# Generate UserPasswords.csv
with open(passwords_file, mode="w", newline="") as passwords_csv:
    writer = csv.writer(passwords_csv)
    # Write header
    writer.writerow(["userId", "passwordHash"])
    # Generate rows
    for user_id in range(1, num_users + 1):
        password = f"Password{user_id}"
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        writer.writerow([user_id, password_hash])

print(f"Generated {users_file} and {passwords_file} successfully.")
