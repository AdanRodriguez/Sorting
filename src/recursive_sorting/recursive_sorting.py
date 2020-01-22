# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    #initialize array indexes
    i_A = 0
    i_B = 0

    #length of the merge array
    for i in range(elements):
        # if an index lies beyond the bounds of the array,
        # we've reached the end, so add element from the other array
        if len(arrA) <= i_A:
            # add element to the merged array and shift index
            merged_arr[i] = arrB[i_B]
            i_B += 1
        elif len(arrB) <= i_B:
            merged_arr[i] = arrA[i_A]
            i_A += 1
            # compare the two smallest unmerged values
        elif arrB[i_B] < arrA[i_A]:
            #if the right side is smaller
            merged_arr[i] = arrB[i_B]
            i_B += 1
        else:
            #if the left side is smaller
            merged_arr[i] = arrA[i_A]
            i_A += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #if the array has one element, it is sorted
    if len(arr) <= 1:
        return arr
    #if array has more than 1 element, split in half, sort each half and then merge
    else:
        mid = len(arr) // 2
        arr_left = arr[:mid]
        arr_right = arr[mid:]
        return merge(merge_sort(arr_left), merge_sort(arr_right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
