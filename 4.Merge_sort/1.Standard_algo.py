def merge(arr,p,q,r):
    arr_L = arr[p:q+1]
    arr_R = arr[q+1:r+1]
    
    L = R = 0
    k = p 
    
    while L < len(arr_L) and R < len(arr_R):
        if arr_L[L] <= arr_R[R]:
            arr[k] = arr_L[L]
            L += 1 
        else:
            arr[k] = arr_R[R]
            R += 1
        k+=1 
    
    while L < len(arr_L):
        arr[k] = arr_L[L]
        L += 1
        k += 1 
        
    while R < len(arr_R):
        arr[k] = arr_R[R]
        R += 1 
        k += 1 
    
def merge_sort(arr,p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)

a = [8, 3, 5, 4, 7, 6, 1, 2]
merge_sort(a, 0, len(a) - 1)
print(a)