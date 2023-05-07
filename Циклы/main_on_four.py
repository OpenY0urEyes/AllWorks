def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print(True)
            return
    print(False)


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
binary_search(arr, 14)  
binary_search(arr, 5)   