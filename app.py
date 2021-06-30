from setting import (PASSWORD_INVALID, USERNAME_EXIST,
                                    USERNAME_NOT_EXIST, LOGIN_OK, REGISTER_OK)


def find_username(user_pass):
    return user_pass[:user_pass.index(":")]


def find_password(user_pass):
    return user_pass[user_pass.index(":")+1:]


def login(username: str, password: str):
    with open("user.txt", "r") as f:
        user_pass_list = f.read()
        if user_pass_list:
            user_pass_list = user_pass_list.split("\n")
            username_list = list(map(find_username, user_pass_list))
            password_list = list(map(find_password, user_pass_list))
            if username in username_list:
                user_name_index = username_list.index(username)
                if password == password_list[user_name_index]:
                    return LOGIN_OK
                else:
                    return PASSWORD_INVALID
            else:
                return USERNAME_NOT_EXIST
        else:
            return USERNAME_NOT_EXIST


def register(username: str, password: str):
    with open("user.txt", "r") as f:
        user_pass_list = f.read()
        if user_pass_list:
            user_pass_list = user_pass_list.split("\n")
            username_list = list(map(find_username, user_pass_list))
            # password_list = list(map(find_password, user_pass_list))
            if username not in username_list:
                with open("user.txt", "a") as f:
                    f.write(f"\n{username}:{password}")
                    return REGISTER_OK
            else:
                return USERNAME_EXIST

def is_blocked(username):
    pass


def freedom(username):
    pass


if __name__ == "__main__":
    find_username
    find_password