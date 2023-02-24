print("Login Authentication")
valid_id = "AliasgerB"
valid_pass = "-A1li@sge3939"
user_id = str(input("Enter Username : "))
user_pass = str(input("Enter password : "))
u_id = False
u_pass = False
if user_id == valid_id :
    if user_pass == valid_pass :
        print("This is the list of all Admin tools")
        print("1 = create a book\n2 = view all books")
        tool = int(input("Selected tool : "))
        if tool == 1 :
            book_name = str(input("Enter book name"))
            content = str(input("Enter Content :"))
            with open(book_name, "w") as file :
                file.write(content)
else :
    if user_id != valid_id :
        user_id = str(input("Enter Username : "))
        if user_id == valid_id :
            u_id = True
    else :
        print("password is incorrect!")
    if user_pass != valid_pass :
            user_pass = str(input("Enter password : "))
            if user_id == valid_id :
                u_pass = True
    else :
        print("Username is incorrect!")
if u_id == True and u_pass ==  True :
    print("This is the list of all Admin tools")
    print("1 = create a book\n2 = view all books")
    tool = int(input("Selected tool : "))
    if tool == 1 :
        book_name = str(input("Enter book name"))
        content = str(input("Enter Content :"))
        with open(book_name, "w") as file :
            file.write(content)
