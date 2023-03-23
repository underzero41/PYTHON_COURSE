def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        more = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)
print(quick_sort([14,5,9,6,3,58,7,6,4,3]))