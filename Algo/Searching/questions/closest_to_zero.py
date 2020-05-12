def minAbsSumPair(arr): 
    size = len(arr)
    if size < 2: 
        print("Invalid Input") 
        return
  
    min_l, min_h = 0, 1
    min_sum = arr[0] + arr[1] 
    for l in range (0, size - 1): 
        print(min_sum)
        for h in range (l + 1, size): 
            sum = arr[l] + arr[h]                  
            print("\t", sum)
            if abs(min_sum) > abs(sum):          
                min_sum = sum
                min_l, min_h = l, h 
  
    print("The two elements whose sum is minimum are", arr[min_l], " & ", arr[min_h]) 
  
def minAbsSumPair2(arr):
    size = len(arr)
    if size < 2: 
        print("Invalid Input") 
        return
    arr.sort()
    l, h = 0, size-1
    min_l, min_h = l, h
    temp_sum, min_sum = 0, 10**9
    if abs(temp_sum) < abs(min_sum): 
            min_sum = temp_sum
            min_l = l 
            min_h = h 
    if(temp_sum < 0): 
        l += 1
    else: 
        h -= 1
    print("The two elements whose sum is minimum are", arr[min_l], " & ", arr[min_h]) 

arr = [1, 60, -10, 70, -80, 85] 
  
#minAbsSumPair(arr)
minAbsSumPair2(arr)

