def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + middle + quick_sort(right)

array = [1, 123, 22, 4124, 1, 2, 3, 4, 666]
print(quick_sort(array))
