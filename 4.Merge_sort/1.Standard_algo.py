def merge(A, p, q, r):
    #A = [8,3]
    L = A[p:q+1] #[8]         
    R = A[q+1:r+1] #[3]      

    i = j = 0  #i is the position for L & j is the position for R        
    k = p               

    while i < len(L) and j < len(R):   
        if L[i] <= R[j]:              
            A[k] = L[i]                
            i += 1                     
        else:                           
            A[k] = R[j]               
            j += 1                     
        k += 1                         

    while i < len(L):                  
        A[k] = L[i]                    
        i += 1                         
        k += 1                         

    while j < len(R):                 
        A[k] = R[j]                    
        j += 1                         
        k += 1                         


def merge_sort(A, p, r):
   
    if p < r:                          
        q = (p + r) // 2               
        merge_sort(A, p, q)           
        merge_sort(A, q + 1, r)        
        merge(A, p, q, r)              

a = [8, 3, 5, 4, 7, 6, 1, 2]
merge_sort(a, 0, len(a) - 1)
print(a)