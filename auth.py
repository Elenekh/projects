import json


def regirster(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data =  {"usernames": [], "passwords": []}

    while True:
        username = input("Choose your username: ").strip()
        password = input("choose your password: ").strip()

        if username in data["usernames"]:
            print("username already taken!")
        else:
            data["usernames"].append(username)
            data["passwords"].append(password)

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"Registration successful! Welcome, {username}")
            break

def login(filename):
    try:
        with open(filename, 'r')as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No users found register first.")
        return
    
    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if username in data["usernames"]:
            index = data["usernames"].index(username)
            if data["passwords"][index] == password:
                print(f"Welcome back {username}")
                return username
        else:
            print("incorrect password!")
