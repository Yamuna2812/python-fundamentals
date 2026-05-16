def subset_sum(arr, target):
    dp = [[False]*(target+1) for _ in range(len(arr)+1)]

    for i in range(len(arr)+1):
        dp[i][0] = True

    for i in range(1, len(arr)+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(arr)][target]


arr = [3, 34, 4, 12, 5, 2]
target = 9

print("Subset exists:", subset_sum(arr, target))
