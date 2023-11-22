class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = set() # using set for unique set of 3 sum
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i+1, len(nums) - 1
            while l < r:
                sum_two = nums[l] + nums[r]
                if sum_two < target:
                    l += 1
                elif sum_two > target:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        # convert set into list
        output = []
        for each in res:
            output.append(list(each))
        return output