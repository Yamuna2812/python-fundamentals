def combination_sum(candidates, target):
    result = []

    def backtrack(remain, path, start):
        if remain == 0:
            result.append(path)
            return
        if remain < 0:
            return

        for i in range(start, len(candidates)):
            backtrack(remain - candidates[i], path + [candidates[i]], i)

    backtrack(target, [], 0)
    return result


print(combination_sum([2,3,6,7], 7))
