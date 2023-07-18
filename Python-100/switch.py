x = int(input("number: "))

match(x/10):

    case 9:
        print("hi")
    case 1:
        print("hello")
    case _ if x > 90 and x < 100:
        print("awesome")
    case _:
        print("default")
