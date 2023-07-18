#strings method
a="helloudoy!!!ee"

print(len(a))

print(a.upper())

print(a.lower())

print(a.rstrip("ee")) #remove the last part of string

print(a.replace("udoy","Yena")) # replace the string

print(a.split(" "))#make a list

print(a.rsplit(" "))#make a list


print(a.capitalize())

print(len(a.center(5)))

print(a.count("e"))#counting element

print(a.startswith("he"))#if exist then true

print(a.endswith("ee"))# if exists  then true

print(a.find("udoy"))#if dont find retuen -1

print(a.isalnum())#true return if string has a-z or A-Z

print(a.islower())

print(a.isupper())

print(a.isprintable())

print(a.isspace()) # if space exist then true

print(a.istitle())

print(a.swapcase())#upper to lower lower to upper



print(a.title())

#turns all fisrt letter of every word into capital letter