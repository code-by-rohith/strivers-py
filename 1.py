def findMaxConsecutiveOnes(nums):
    cnt = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        else:
            cnt = 0
        maxi = max(maxi, cnt)
    return maxi


num = input("Enter a list : ")
nums = list(map(int, num.split()))
ans = findMaxConsecutiveOnes(nums)
print("The maximum  consecutive 1's are", ans)