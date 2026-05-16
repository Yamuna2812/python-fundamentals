def find_median(arr1, arr2):
    merged = sorted(arr1 + arr2)
    n = len(merged)

    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        return merged[n//2]


arr1 = [1, 3]
arr2 = [2]

print("Median:", find_median(arr1, arr2))
