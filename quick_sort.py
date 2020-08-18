
# What do we need for a recursive function?
## Base case
## Function that calls itself
# Progress toward base case

# Often elegant, terse, few lines of code

# Divide and conquer!
## Can divide into subproblems that have the same "shape" as the parent problem
## solve subproblems
## combine your solutions, the overall problem is solved

# if finding most efficient route to deliver all mail at once?
## divide into subregions
## find most efficient route in each subregion
## now you've delivered all the mail!

# Sortiing
## Break up the array
## sort each piece
## put them back together again

# choose your pivot: median, or first or last number in array
arr = [5, 7, 3, 1, 2, 9, 0, 8, 4, 6]
pivot = arr[0]

'''        [3,1,2,0,4]    [5]    [7,9,8,6]
[3,1,2,0,4]
pivot = arr[0]
        [0,1,2]    [3]    [4] ...repeat until only 1 thing on the left
...[0] [1] [2]
pivot = arr[0]
left=[]
right=[]
return [0] + [1] + [2]  ==> [0, 1, 2]
'''

def partition(arr):
    ## choose pivot
    pivot = arr[0]
    left = []
    right = []
    ## partition around the pivot 
    for num in arr:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)

    return (left, pivot, right)

# QuickSort
def quicksort(arr):
    ## Base case: empty array
    if len(arr) == 0:
        return arr

    ## recurse on left and later right sides
    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(arr))