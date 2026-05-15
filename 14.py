import heapq

def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]


arr = [3, 2, 1, 5, 6, 4]
k = 2

print("Kth largest:", kth_largest(arr, k))
