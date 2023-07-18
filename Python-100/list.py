'''list in python'''
marks=[1,2,3,"hello","udoy"]

if 7 in marks:
    print("yes")
else:
    print("no")

'''list methods'''

l=[23,45,1,2,3,4]

print(l)

l.append(7)

print(l)

l.sort()

print(l)

l.reverse()

print(l)

print(l.index(1))

print(l.count(23))

m=l.copy()
print(m)

l.insert(3,500)
print(l)

m=[23,34,45]

l.extend(m)#put m in the last of l

print(l)

k=l+m
print(k)

print(k.__len__())