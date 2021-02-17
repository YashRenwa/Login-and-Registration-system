def register():
    user_name = input("User Name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    if password == confirm_password:
        user_info = [f"{user_name}\n", f"{email}\n", f"{password}\n"]
        users = open("users.txt", "a")
        users.writelines(user_info)
        print("Registration Successful :)")
    else:
        print('''
            Passwords doesn't match!!
            Registration failed :(
            ''')


def login():
    user_name = input("User Name: ")
    password = input("Password: ")
    users = open("users.txt", "r")
    users_info = users.readlines()
    for user_index in range(len(users_info)-1):
        if users_info[user_index].rstrip("\n") == user_name:
            if users_info[user_index+2].rstrip("\n") == password:
                print("\nLogin Successful!!!")
                print(f"Welcome {user_name.upper()}")
                break
    else:
        print("Login Failed :(")


print('''
Welcome to Dashboard.
Already a user? Type login.
New here? Type register.''')
check = input()

if check.lower() == "register":
    register()
elif check.lower() == "login":
    login()
else:
    print(f"What the hell is {check}!!!!")
