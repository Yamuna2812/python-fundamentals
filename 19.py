def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    return -1


arr = sorted(list(map(int, input("Enter sorted numbers: ").split())))
key = int(input("Enter key: "))

print("Index:", binary_search(arr, 0, len(arr) - 1, key))
