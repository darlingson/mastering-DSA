def quicksort(array):
    if len(array) <= 1:
        return array
    less_than_pivot = []
    greater_than_pivot = []
    pivot = array[0]
    for value in array[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

numbers = [2,199,45,38,3]
sorted_numbers =quicksort(numbers)
print(sorted_numbers)