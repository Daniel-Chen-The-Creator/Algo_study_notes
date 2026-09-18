def sort_moves(arr):
    moves = 0
    for i in range(len(arr)):
        key = arr[i] 
        j =  i - 1
        while j >= 0 and arr[j] > key:
            moves += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr,moves
nums = [5,6,3,1,2,]
nums,moves = sort_moves(nums)
print(nums)
print(moves)

            
            