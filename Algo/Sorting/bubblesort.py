#My implementation of bubble sort algo
def bubbleSort(arr):
    size = len(arr) 
    if size < 2:
        print("Sorting not possible")
        return
    count = 0
    for i in range(0, size):  #for sorted elements at the end
        count += 1
        for j in range(0, size-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count

def reversedBubbleSort(arr):
    size = len(arr) 
    if size < 2:
        print("Sorting not possible")
        return
    count = 0
    for i in reversed(range(0, size)):  #for sorted elements at the end  #decrementing for
        count += 1
        for j in range(0, i-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count

def optimizedBubbleSort(arr):
    size = len(arr) 
    if size < 2:
        print("Sorting not possible")
        return
    count = 0
    for i in range(0, size):  #for sorted elements at the end
        flag = 0
        count += 1
        for j in range(0, size-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            return arr, count
    #return arr, count




a = [-1,0,1,2,12,32,52,10,22,3,5,13,7,9,4]
print(bubbleSort(a))
a = [-1,0,1,2,12,32,52,10,22,3,5,13,7,9,4]  #reintialize coz of inplace sorting
print(reversedBubbleSort(a))
a = [-1,0,1,2,12,32,52,10,22,3,5,13,7,9,4]  #reintialize coz of inplace sorting
print(optimizedBubbleSort(a))
