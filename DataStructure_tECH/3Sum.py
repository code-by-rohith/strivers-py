from typing import  List
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        if len(nums) < 3:
            return []
        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            a = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,1]
    print(f"Input: {nums}")
    print("Output:", sol.threeSum(nums))
