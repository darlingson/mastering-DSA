def merge_sort(arr):
    """
    Sorts an array in ascending order
    Returns a new sorted array

    Divide : Find the mid point of the array and divide into sub arrays
    Conquer: Recursively sort the sub arrays created in previous step
    Combine: Merge the sorted sub arrays created in previous step
    """
    if len(arr) <= 1:
        return arr
    
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(arr):
    """
    Divide the unsorted list at midpoint into sub list
    Returns two sub lists
    """
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return left, right
def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(l)