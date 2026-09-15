arr = [2,1,4,19,20,14,10,99,24]
for i in range(len(arr)):
    key = arr[i]
    j = i - 1 
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1 
    arr[j + 1] = key
print(arr)


