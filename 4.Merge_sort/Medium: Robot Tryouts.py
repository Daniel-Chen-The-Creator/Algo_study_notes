def merge(arr,p,q,r):
    arr_l = arr[p:q+1]
    arr_r = arr[q+1:r+1]
    l = r = 0
    k = p 
    while l < len(arr_l) and r < len(arr_r):
        if arr_l[l][0] > arr_r[r][0]:
            arr[k] = arr_l[l]
            l += 1 
        elif arr_l[l][0] == arr_r[r][0]:
            if arr_l[l][1] <= arr_r[r][1]:
                arr[k] = arr_l[l]
                l += 1 
            else:
                arr[k] = arr_r[r]
                r += 1 
        else:
            arr[k] = arr_r[r]
            r += 1 
        k += 1 
    while l < len(arr_l):
        arr[k] = arr_l[l]
        l += 1 
        k += 1 
    while r < len(arr_r):
        arr[k] = arr_r[r]
        r += 1 
        k += 1
            
def merge_sort(arr,p,r):
    if p < r:
        q = (p + r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q + 1,r)
        merge(arr,p,q,r)
    
    
def take_input():
    n = int(input())
    arr = []
    for i in range(n):
        student = list(map(int,input().split()))
        student.append(i+1)
        arr.append(student)
        
    return arr

def output(arr):
    for a in arr:
        print(a[2],end=" ")
    print()
        
arr = take_input()
merge_sort(arr,0,len(arr) - 1)
output(arr)
#[[90, 120], [95, 150], [90, 100], [95, 150], [90, 100], [80, 90]]