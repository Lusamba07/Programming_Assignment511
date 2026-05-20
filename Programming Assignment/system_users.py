def registration():
    print("\n=== Customer Registration ===")

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful!")


def sign_in():
    print("\n=== SignIn ===")

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    signin_success = False

    for user in users:

        stored_username, stored_password = user.strip().split(",")

        if username == stored_username and password == stored_password:
            signin_success = True
            break

    if not signin_success:
        print("Invalid username or password")
    else:
        print("SignIn successful!")

