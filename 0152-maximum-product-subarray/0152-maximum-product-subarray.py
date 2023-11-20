class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for each in nums:
            temp = each*currMax
            currMax = max(each*currMax, each*currMin, each)
            currMin = min(temp, each*currMin, each)
            res = max(res, currMax)
        return res
        