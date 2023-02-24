import os
while True:
    print("Login Authentication")
    valid_id = "AliasgerB"
    valid_pass = "-A1li@sge3939"
    lim = 3
    auth = False
    while lim != 0:
        user_id = (input("Enter Username : "))
        user_pass = (input("Enter password : "))
        if user_id == valid_id:
            if user_pass == valid_pass:
                auth = True
                break
            else:
                print('Incorrect Password')
                lim -= 1
                continue
        else:
            print('Incorrect Username.')
            lim -= 1
            continue
    if auth:
        print("This is the list of all Admin tools")
        print("1 = create a book\n2 = view all books")
        tool = int(input("Selected tool : "))
        if tool == 1:
            print(" c = create book\n r = remove book\n mr = remove multiple book")
            diract = (input("Enter function : "))
            if diract == "c":
                print("out = stop creating book")
                while True:
                    print(
                        "emp = make empty book\nwp = with pages\neep = edit existing page")
                    book_type = input("Selected : ")
                    if book_type == "wp":
                        is_exit = input("Are you want to exit write" +
                                        "\033[1m" + " out" + "\033[0m" + ": ")
                        if is_exit == "out":
                            break
                        else:
                            book_name = (input("Enter book name : "))
                            path = f"files/{book_name}"
                            os.mkdir(path)
                            print(
                                "cr = create a page\ne = edit page\no = open page\ncp = copy content of page")
                            fileact = (input("Enter action to perform : "))
                            if fileact == "cr":
                                file_name = (input("Enter page name : "))
                                content = (input("Enter Content :"))
                                with open(f"files/{book_name}/{file_name}.txt", "w") as file:
                                    file.write(content)
                            elif fileact == "e":
                                file_name = (input("Enter page name : "))
                                content = (input("Enter Content :"))
                                with open(f"files/{book_name}/{file_name}.txt", "a") as file:
                                    file.write(content)
                            elif fileact == "o":
                                read = input("enter page name to view : ")
                                readFile = f"files/{book_name}/{read}.txt"
                                for line in readFile:
                                    print(line.strip())
                            elif fileact == "rm":
                                while True:
                                    is_exit = input("Are you want to exit write" +
                                                    "\033[1m" + " out" + "\033[0m" + ": ")
                                    if is_exit == "out":
                                        break
                                    else:
                                        rmPage = input(
                                            "Enter Page name to remove : ")
                                        os.remove(rmPage)
                    elif book_type == "emp":
                        is_exit = input("Are you want to exit write" +
                                        "\033[1m" + " out" + "\033[0m" + ": ")
                        if is_exit == "out":
                            break
                        else:
                            book_name = (input("Enter book name : "))
                            path = f"files/{book_name}"
                            os.mkdir(path)
                    elif book_type == "eep":
                        print("rm = remove page, o = open page")
                        removePage = input("select option : ")
                        if removePage == "rm":
                            while True:
                                is_exit = input("Are you want to exit write" +
                                                "\033[1m" + " out" + "\033[0m" + ": ")
                                if is_exit == "out":
                                    break
                                else:
                                    rmPage = input("Enter book name : ")
                                    rmPage2 = input(
                                        "Enter Page name to remove : ")
                                    path = f"files/{rmPage}/{rmPage2}"
                                    os.remove(path)
                        elif removePage == "o" :
                            book_n = input("enter book name : ")
                            read = input("enter page name to view : ")
                            readFile = f"files/{book_n}/{read}.txt"
                            for line in readFile:
                                print(line.strip())
                        is_exit = input("Are you want to exit write" +
                                        "\033[1m" + " out" + "\033[0m" + ": ")
                        if is_exit == "out":
                            break
                        else:
                            book = input("Enter book name: ")
                            if not book:
                                print("Book name cannot be empty")
                                continue
                            page = input("Enter page name: ")
                            if not page:
                                print("Page name cannot be empty")
                                continue
                            page_with_path = f"files/{book}/{page}"
                            try:
                                with open(page_with_path, 'r') as f:
                                    for line in f:
                                        print(line.strip())
                            except FileNotFoundError:
                                print(f"File not found: {page_with_path}")
                            except Exception as e:
                                print(
                                    f"Error reading file: {page_with_path} - {e}")
            if diract == "r":
                rmBook_name = (input("Enter book name : "))
                delpath = f"files/{rmBook_name}"
                os.rmdir(delpath)
            if diract == "mr":
                print("out = stop removing book")
                while True:
                    mlutiRemove = (input("Enter Book name : "))
                    list_file = os.listdir(f"files/{mlutiRemove}")
                    if len(list_file) != 0:
                        for lf in list_file:
                            os.remove(f"files/{mlutiRemove}/{lf}")
                            os.rmdir(f"files/{mlutiRemove}")
                            is_exit = input(
                                "Are you want to exit write" + "\033[1m" + " out" + "\033[0m" + ": ")
                            print(is_exit)
                            if is_exit == "out":
                                break
                        break
                    else:
                        os.rmdir(f"files/{mlutiRemove}")
        if tool == 2 :
            lst = os.listdir("files")
            for i in lst :
                print(i)
                print("-------------------------------------------------------------")
    else:
        print("Too many attempts")

    # content = (input("Enter Content :"))
    # with open("files/" + book_name, "w") as file :
    # file.write(content)
