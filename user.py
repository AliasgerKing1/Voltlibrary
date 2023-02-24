import os

while True:
    print("log = Login\nreg = register")
    mode = input("Enter mode : ")
    if mode == "reg":
        print("\033[1m" + "Registration : " + "\033[0m")
        user_id = input("Enter your username: ")
        user_pass = input("Enter your password: ")
        with open("logindetails/login", "a") as file:
            file.write(f"{user_id}::{user_pass}\n")
    if mode == "log":
        print("Login Authentication")
        valid_ids = []
        valid_passwords = []
        with open("logindetails/login", "r") as file:
            for line in file:
                user_id, user_pass = line.strip().split("::")
                valid_ids.append(user_id)
                valid_passwords.append(user_pass)
        lim = 3
        auth = False
        while lim != 0:
            user_id = input("Enter username: ")
            user_pass = input("Enter password: ")
            if user_id in valid_ids:
                index = valid_ids.index(user_id)
                if user_pass == valid_passwords[index]:
                    auth = True
                    break
                else:
                    print('Incorrect Password.')
                    lim -= 1
                    continue
            else:
                print('Incorrect Username.')
                lim -= 1
                continue
        if auth:
            print("Authentication successful")
            ubook_name = input("enter book name tha you want to read: ")
            book_item_list = f"files/{ubook_name}"
            page_name = input("Enter page name: ")
            full_page = f"{page_name}.txt"
            lst = os.listdir(book_item_list)
            found = False

            for file in lst:
                if file == full_page:
                    with open(os.path.join(book_item_list, full_page), "r") as f:
                        content = f.read()
                        print(f"{page_name}:")
                        print(content)
                        found = True
                        break

            if not found:
                print("Page not found.")
        else:
            print("Invalid selection.")
    else:
        print("Too many attempts")
