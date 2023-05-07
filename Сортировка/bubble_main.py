def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr



array = [1, 123, 22, 4124, 1, 2, 3, 4, 666]

print(bubble_sort(array))
