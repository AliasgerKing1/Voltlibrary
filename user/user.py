print("Login Authentication")
valid_id = "AliasgerB"
valid_pass = "-A1li@sge3939"
user_id = str(input("Enter Username : "))
user_pass = str(input("Enter password : "))
u_id = False
u_pass = False
if user_id == valid_id :
    if user_pass == valid_pass :
        print("true")
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
    print("true")
