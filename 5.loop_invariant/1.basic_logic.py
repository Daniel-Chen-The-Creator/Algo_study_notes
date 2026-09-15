# Loop Invariant
#
# A loop invariant is something that stays true
# ——————before and after every iteration of a loop.
#
# In simple words:
# It is a rule or condition that the loop keeps maintaining.
#
#
# Example:  Insertion Sort
#
#           Loop invariant:
#           Before each iteration, arr[0:i] is already sorted.
#
#           We usually prove a loop invariant in 3 steps:
#
#           1. Initialization
#               The invariant is true before the loop starts.
#
#           2. Maintenance
#               If the invariant is true before one iteration,
#               the loop keeps it true after that iteration.
#
#           3. Termination
#               When the loop ends, the invariant helps us prove
#               that the algorithm is correct.


arr = [99, 5, 2, 0, 1, 3, 1, 4]

for i in range(len(arr)):

    # LOOP INVARIANT:
    # At this point, arr[0:i] is sorted.

    current_insertion = arr[i]
    previous_element = i - 1

    # Move elements that are larger than current_insertion
    # one position to the right.
    while (
        previous_element >= 0
        and arr[previous_element] > current_insertion
    ):
        arr[previous_element + 1] = arr[previous_element]
        previous_element -= 1

    # Insert current_insertion into the correct position.
    arr[previous_element + 1] = current_insertion

    # After this iteration:
    # arr[0:i+1] is sorted.


print(arr)