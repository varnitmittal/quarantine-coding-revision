a = [15,5,20,35,2,42,67,17]

key = 42
flag = 0

for i in range(len(a)):
    if(key == a[i]):
        print("Found at index ", i)
        flag = 1

if(flag == 0):
    print("Not Found!")
