# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #elements = len(arrA) + len(arrB)
    merged_arr = []# * elements
    l = len(arrA)
    r = len(arrB)
    arrA_index = 0
    arrB_index = 0
    while (arrA_index < l and arrB_index < r):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
    # Your code here


    return merged_arr + arrA[arrA_index:] + arrB[arrB_index:]

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        l = merge_sort(arr[:mid])
        r = merge_sort(arr[mid:])
        return merge(l, r)

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

