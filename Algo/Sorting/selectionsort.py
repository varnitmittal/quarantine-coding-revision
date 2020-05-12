def selectionSort(arr):
    size = len(arr)
    for i in range(0, size):
        minIndex = i
        for j in range(i+1, size):
            if arr[j] < arr[minIndex]: 
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
a = [12,32,52,10,22,3,5,13,7,9,4]
print(selectionSort(a))