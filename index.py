import sys
import time
import os
sys.path.append('./admin')
sys.path.append('./user')
os.system("cls")
print("wait for some second we are opening your terminal !")
for i in range(0, 110,10) :
    for y in range(1,5) :
        loading= f"|{'#'*int(i/10)}"
        if y == 1 :
            c = "/"
        elif y == 2 :
            c = "|"
        elif y == 3 : 
            c = "\\"
        else : 
            c = "-"
        print(loading.ljust(12),'|',c ,i, "%")
        time.sleep(0.1/3)
        os.system("cls")


# for i in range(0, 100,10) :
#     for y in range(1,4) :
#         loading= f"Loading{'.'*y}"
#         print(loading.ljust(10) ,i, "%")
#         time.sleep(0.1/3)
#         os.system("cls")



time.sleep(1.5)
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
