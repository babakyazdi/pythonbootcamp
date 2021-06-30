from app import login, register
from setting import (PASSWORD_INVALID, USERNAME_EXIST,
                                    USERNAME_NOT_EXIST, LOGIN_OK, REGISTER_OK)



user_login_status = {}

while True:
    entry_point = input('''
                         Welcome to My Calculator

                for login use "L" and for register use "R"

            ''')

    if entry_point == 'L':
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            with open("blocked.txt", "r") as f:
                block_list = f.read()
                if username in block_list:
                    print("You are blocked")
                    continue
        except FileNotFoundError:
            open("blocked.txt", "x")

        login_status = login(username, password)
        if login_status == LOGIN_OK:
            print(f"Hello {username}")
            break
        elif login_status == PASSWORD_INVALID:
            if username in user_login_status:
                if user_login_status[username] == 3:
                    print("You are blocked")
                    with open("blocked.txt", "a") as f:
                        f.write(f"\n{username}")
                else:
                    print("Username not valid")
                    user_login_status[username] += 1
                continue
            else:
                user_login_status[username] = 1
            print("username or password is invalid. try again!")
            continue
        elif login_status == USERNAME_NOT_EXIST:
            print("username not valid !")
            continue
    elif entry_point == "R":
        username = input("Enter username: ")
        password = input("Enter password: ")
        password2 = input("Enter password again: ")
        
        if ":" in username or ":" in password:
            print("username or password can not have ':'")
        elif password != password2:
            print("passwords must match!")
        elif len(password)<8:
            print("password must have 8 or more characters!")
        else:
            register_status = register(username, password)
            if register_status == REGISTER_OK:
                print(f"Welcome {username}")
                break
            elif register_status == USERNAME_EXIST:
                print("this user exists!")
                continue
    else:
        print("Only L or R !")
