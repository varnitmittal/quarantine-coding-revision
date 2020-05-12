a = [15,5,20,35,2,42,67,17]
key = 422

def linear_search(a, key, index=0):
    if index >= len(a):
        return -1
    elif a[index] == key:
        return index
    else:
        return linear_search(a, key, index+1)

r = linear_search(a, key)
if r == -1:
    print("Element not found!")
else:
    print("Element {} found at index {}".format(key, r))