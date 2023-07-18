# if-else///else-if///nested///
a = int(input("enter your age: \n"))

# print(" your age: ", a)

# if (a > 18):
#     print("you can give vote\n")  # space is indentation....

# else:
#     print("not")


# else-if:

b = int(input("enter your age: \n"))

# if (a > b):
#     print("greater a")
# elif (a == b):
#     print("same")
# else:
#     print("b grater")


# nested elif:

if(a<b):
    print("sorry,welcome")

elif(a>b):
    
    c = int(input("enter your age: \n"))

    if(b==c):
        print("bye")
    else:
        print("tata")

else:
    print("equal")