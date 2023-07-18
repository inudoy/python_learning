
name=input("enter your name: ")
import time
currentt=time.strftime("%H:%M:%S")
print((currentt))
hours=int(time.strftime("%H"))

if(hours>=0 and hours<12):
    print("good morning",name)
elif(hours>=12 and hours<17):
    print("good noon",name)
elif(hours>=17 and hours<20):
    print("good evening",name)
elif(hours>=20 and hours<=24):
    print("good night",name)
else:
    print("invalid")

