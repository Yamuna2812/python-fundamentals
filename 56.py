import heapq

def median_sliding(nums, k):
    result = []

    for i in range(len(nums) - k + 1):
        window = sorted(nums[i:i+k])
        mid = k // 2
        if k % 2 == 0:
            result.append((window[mid-1] + window[mid]) / 2)
        else:
            result.append(window[mid])

    return result


print(median_sliding([1,3,-1,-3,5,3,6,7], 3))
