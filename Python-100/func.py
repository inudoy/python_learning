'''default arguement
keyword arguement
variable arguement
required variable'''

def cal(a,b):
    mean=(a*b)/(a+b)
    print(f"mean=%.4f"%mean)
    print(f"mean={mean:.4f}")
def isgreat(a,b):
    if(a>b):
        print("a is bigger")
    else:
        print("b is bigger")
def isless(a,b):
    pass  #'''means it will do the code later'''
a=9
b=10
cal(a,b) 
isgreat(a,b)