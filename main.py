import hashlib
Sample stored user data (username and hashed password)
users = {
"admin": hashlib.sha256("password123".encode()).hexdigest()
} def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
 if username in users and users[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")
      login()
