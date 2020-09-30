l = [8, 2, 5, 4, 1, 3]

print(l)
# Implement an insertion sort algorithm
def insertion_sort(list_to_sort):
    # seperate the first element and think of it as sorted
    # Let us say i is the first item in the list
    # for all other items (on the right of the first index)
    # range based starting at index 1
    for i in range(1, len(list_to_sort)):
        # put the current number in a temp variable
        temp = list_to_sort[i]
        # keep track of our index as j
        j = 1
        # keep looking left, until we find where our temp number belongs
        # while j is greater than zero (we are not past the start of the index)
        # and our temp variable is less than the num to the left of j
        while j > 0 and temp < list_to_sort[j-1]:
            # as we look left we can shift the items to right as we iterate
            list_to_sort[j] = list_to_sort[j-1]
            # decrement 
            j -= 1
        # when lefy is smaller than temp, or we are at zero, put the item at that spot
        list_to_sort[j] = temp
    # return the list back to the caller
    return list_to_sort

# lets try it
insertion_sort(l)

print(l)