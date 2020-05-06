#Other useful methods
a = [25, 12, 36, 11, 39, 24, 5, 9, 6, 10]

print(sum(a))

print(a.count(36)) 

print(len(a))

print(a.index(24))

print(min(a))

print(max(a))


def sq(n):
    return n*n

b = [1,2,3,4]

result = map(sq, b)

print(result)

bsq = set(result)
print(bsq)