#Sep 12 Notes

arr = [2,1,4,19,20,14,10,99,24]
for i in range(len(arr)): # i = 5
    key = arr[i]  #key = 14
    j = i - 1  # j = 4
    while j >= 0 and arr[j] > key: #j = 4 & 20 > 14
        arr[j + 1] = arr[j] 
        j -= 1
    arr[j + 1] = key 
    
print(arr)

#//////////////////////////////////////////////////////////////////////////////
#Why using key instead of straightly using arr[i]?
#   ————Because if a value will be overwritten, but you still need it later, 
#       save it in a separate variable before making changes.
#//////////////////////////////////////////////////////////////////////////////

#Base case shows you where the function stops


#Logical code

arr = [99,5,2,0,1,3,1,4]

for i in range(len(arr)):
    current_insertion = arr[i]
    previous_element = i - 1

    while previous_element >= 0 and arr[previous_element] > current_insertion:
        arr[previous_element + 1] = arr[previous_element]
        previous_element -= 1

    arr[previous_element + 1] = current_insertion

print(arr)

#<Introduction to Algorithm> Pg 46