a = [15,5,20,35,2,42,67,17]
a.sort()
print(a)

key = 42

def BS(key, l=0, h=len(a)):
    while(l <= h):
        mid = int((l+h)/2)
        if(a[mid] == key):
            return mid
        elif(a[mid] < key):
            l = mid+1
        else:
            h = mid-1
    return -1

r = BS(key)
if r == -1:
    "Key not found"
else:
    print("Key {} found at index {}".format(key, r))