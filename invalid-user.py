import bcrypt
user_db = {}

_ = ["tina", "mina", "jina", "sina","lina"]
username = input("Enter username: ").strip().lower()

while True:
    password_input = input("Enter password: ").strip()
    if password_input.lower() in _:
        print("Invalid! — password cannot be the name of your spouse or girlfriend.")
    else:
        password = password_input.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        user_db[username] = hashed
        print("\n Registration successful! Welcome to the hood!")
        break
