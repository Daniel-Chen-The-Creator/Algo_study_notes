#Complexity
arr = [1,2,3,4,5,6,7,8]

#1.O(1)
x = arr[0]
y = arr[-1]
print(x + y)

#2. O(logn)
i = len(arr)
while i > 1:
    i //= 2
    
#3. O(n)
for j in range(i):
    print(j)
#or
for e in arr:
    print(e)    

#4. O(nlogn)
for i_1 in range(i):  #O(n)
    j = i_1

    while j > 1:    #O(logn)
        j //= 2
        # n * logn = nlogn

#5. O(n^2)
for k in range(i):
    for j in range(i):
        print(k, j)