#adding elements to list

a = [25,12,36]

a.append(39)
a.append(24)

a.append((3,7))
a.append([4,8])

a.extend((5,9))

a.extend([6,10])

a.insert(3, 11)
a.insert(4, (12,13))
a.insert(5, [14,15])

print(a)