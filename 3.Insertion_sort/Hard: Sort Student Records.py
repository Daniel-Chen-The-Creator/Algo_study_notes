def Sort_student_records(arr):
    for i in range(len(arr)):
        key_arr = arr[i]
        print(arr[i][1])
        # name,score,age = key_arr
        j = i - 1
        while j >= 0:
            if arr[j][1] < key_arr[1]:
                arr[j + 1] = arr[j]
                j -= 1
            elif arr[j][1] == key_arr[1]:
                if arr[j][2] > key_arr[2]:
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break        # wrong if you do j -= 1
            else:
                break           # wrong if you do j -= 1 because when j == -1, it ends the while loop, but if you take a loom at line 19:
        arr[j + 1] = key_arr    # arr[j + 1] = arr[0] would be covered by key_arr
    return arr
    
arr = [
    ["Amy", 85, 19],
    ["Ben", 92, 20],
    ["Cara", 85, 18],
    ["Dan", 92, 18],
    ["Eva", 85, 18],
    ["Finn", 78, 19]
]
arr = Sort_student_records(arr)
print(arr)
                

# Funciton of break:
# using in both while and for loop, it ends the loop immediately