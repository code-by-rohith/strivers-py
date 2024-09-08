def three_sum_bruteforce(nums):
    res = []
    n = len(nums)
    seen = set()  # To track seen triplets

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))  # Sort and convert to tuple
                    if triplet not in seen:
                        seen.add(triplet)
                        res.append(list(triplet))

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum_bruteforce(nums))
