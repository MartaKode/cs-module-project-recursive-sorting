# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if start<= end:
        midpoint = round((start+end)/2)

        if target > arr[midpoint]:
            start = midpoint + 1
            return binary_search(arr, target, start, end)
        if target < arr[midpoint]:
            end = midpoint - 1
            return binary_search(arr, target, start, end)
        # base case: target == arr[midpoint]
        else: 
            return arr.index(target)

    return - 1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    # chekc if arr is empty
    if not len(arr):
        return arr

    start = 0
    end = len(arr)-1

    # check if we're going ascending:
    if arr[0] < arr[len(arr)-1]:
        # old iterative code should work
        while start <= end:
            midpoint = round((start+end)/2)
            if target > arr[midpoint]:
                start = midpoint + 1
            if target < arr[midpoint]:
                end = midpoint - 1
            if target == arr[midpoint]: 
                return arr.index(target)


    # check if we're going descending:
    if arr[0] > arr[len(arr)-1]:
        # do things in reverse!
        while start <= end:
            midpoint = round((start+end)/2)
            if target > arr[midpoint]:
                end = midpoint -1
            if target < arr[midpoint]:
                start = midpoint + 1
            if target == arr[midpoint]: 
                return arr.index(target)

    return -1

ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

print(agnostic_binary_search(ascending, 31))
print(agnostic_binary_search(descending, -3))