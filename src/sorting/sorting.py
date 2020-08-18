# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    empty_arr = []
    # for i in range(0, len(merged_arr)-1):
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            # merged_arr[i] = arrA[0]
            empty_arr.append(arrA[0])
            # arrA.pop(0)
            arrA = arrA[1:]
        else:
            # merged_arr[i] = arrB[0]
            empty_arr.append(arrB[0])
            # arrB.pop(0)
            arrB = arrB[1:]
    # merged_arr = empty_arr
    while len(arrA) > 0:
        empty_arr.append(arrA[0])
        # merged_arr[i] = arrA[0]
        # arrA.pop(0)
        arrA = arrA[1:]
    while len(arrB) > 0:
        empty_arr.append(arrB[0])
        # merged_arr[i] = arrB[0]
        # arrB.pop(0)
        arrB = arrB[1:]

    merged_arr = empty_arr

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: if can't chop in half return arr
    if len(arr) <= 1:
        return arr
    # chop in half
    if len(arr) > 1:
        midpoint = round(len(arr)/2)
        left_chopped = arr[:midpoint]
        right_chopped = arr[midpoint:]
        left_chopped = merge_sort(left_chopped)
        right_chopped = merge_sort(right_chopped)

        # merge sorted halves
        return(merge(left_chopped, right_chopped))

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

# chop in half
# recurse
# base case: nothing more to chop
# sort as you combine together
# look at first thing in combined arrays, separate and put it first
