def main(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum


nums = [1, 4, 3, 2]
print(main(nums))
