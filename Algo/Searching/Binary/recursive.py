a = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]

def DAC_BS(key,l=0, h=len(a)-1):   #large problem in DAC
    if(l == h):  #single element in list
        if(a[l] == key): #small problem in DAC
            return l
        else:
            return -1
    
    mid = int((l+h)/2)
    if(a[mid] == key):   
        return mid 
    elif a[mid] < key:   #key is to the right of mid
        return DAC_BS(key, mid+1, h)
    else:
        return DAC_BS(key, l, mid-1)

key = 42
print(a, "key =", key)
r = DAC_BS(key)
if r == -1:
    print("Key not found")
else:
    print("Key {} found at index {}".format(key, r))
