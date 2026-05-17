def permute(nums):
    result = []

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path)
            return

        for n in nums:
            if n not in path:
                backtrack(path + [n])

    backtrack([])
    return result


print(permute([1,2,3]))
