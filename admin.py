import os
print("Login Authentication")
valid_id = "a"
# AliasgerB
valid_pass = "b"
# -A1li@sge3939
lim = 3
auth=False
while lim!=0:
    user_id = (input("Enter Username : "))
    user_pass = (input("Enter password : "))
    if user_id == valid_id:
        if user_pass == valid_pass:
            print("yess")
            auth=True;
            break
        else:
            print('Incorrect Password');
            lim-=1;
            continue
    else:
        print('Incorrect Username.')
        lim-=1;
        continue
if auth:
    print("This is the list of all Admin tools")
    print("1 = create a book\n2 = view all books")
    tool = int(input("Selected tool : "))
    if tool == 1 :
        print(" c = create book\n r = remove book\n mr = remove multiple book")
        diract = (input("Enter function : "))
        if diract == "c" :
            print("out = stop creating book")
            while True :
                print("emp = make empty book\nwp = with pages")
                book_type = input("Selected : ")
                if book_type == "wp" :
                    is_exit = input("Are you want to exit write" +"\033[1m" + " out" + "\033[0m" + ": ")
                    if is_exit == "out" :
                        break
                    else :
                        book_name = (input("Enter book name : "))
                        path = f"files/{book_name}"
                        os.mkdir(path)
                        print("cr = create a page\ne = edit page\no = open page\nrm = remove page\ncp = copy content of page")
                        fileact = (input("Enter action to perform : "))
                        if fileact == "cr" :
                            file_name = (input("Enter file name : "))
                            content = (input("Enter Content :"))
                            with open(f"files/{book_name}/{file_name}", "w") as file :
                                file.write(content)  
                elif book_type == "emp" :
                    is_exit = input("Are you want to exit write" +"\033[1m" + " out" + "\033[0m" + ": ")
                    if is_exit == "out" :
                        break
                    else :
                        book_name = (input("Enter book name : "))
                        path = f"files/{book_name}"
                        os.mkdir(path)
        if diract == "r" :
            rmBook_name = (input("Enter book name : "))
            delpath = f"files/{rmBook_name}"
            os.rmdir(delpath)
        if diract == "mr" :
            print("out = stop removing book")
            while True :
                mlutiRemove = (input("Enter Book name : "))
                list_file = os.listdir(f"files/{mlutiRemove}")
                if len(list_file) != 0 :
                    for lf in list_file :
                        os.remove(f"files/{mlutiRemove}/{lf}")
                        os.rmdir(f"files/{mlutiRemove}")
                        is_exit = input("Are you want to exit write" +"\033[1m" + " out" + "\033[0m" + ": ")
                        print(is_exit)
                        if is_exit == "out" :
                            break
                    break
                else :
                    os.rmdir(f"files/{mlutiRemove}")

else :
    print("Too many attempts")





            # content = (input("Enter Content :"))
        # with open("files/" + book_name, "w") as file :
            # file.write(content)  