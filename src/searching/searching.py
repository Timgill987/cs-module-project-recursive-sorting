# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, s, e):

    # Your code here
    if s > e:
        return -1

    mid = (s + e) // 2
    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, s, mid-1)
    else:
        return binary_search(arr, target, mid+1, e)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

