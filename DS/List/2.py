#removing elements form list 
a = [25, 12, 36, 11, (12, 13), [14, 15], 39, 24, (3, 7), [4, 8], 5, 9, 6, 10]

a.pop(0)
a.pop(0)
a.pop(2)
print(a.pop(2))

a.pop(-2)
a.pop()

a.remove(5)
a.append(63)
a.append(9)
a.remove(9)

del a[0]
del a[0:3]

del a[0:3:2]
#del a[:]
a.clear()

print(a)