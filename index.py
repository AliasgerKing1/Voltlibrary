import sys
sys.path.append('./admin')
sys.path.append('./user')
VL = "VoltLibrary"
heading = "Welcome to " + "\033[1m" + VL + "\033[0m" + " portal !!!"
print(heading)

print("Select you are Admin or User")
print("1 = Admin\n2 = User")
auth = int(input("select : "))

if auth == 1:
    print("I am Admin")
    import admin
elif auth == 2:
    print("I am User")
    import user
