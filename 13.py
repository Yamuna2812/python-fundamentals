def lis(arr):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


arr = list(map(int, input("Enter numbers: ").split()))
print("LIS length:", lis(arr))
