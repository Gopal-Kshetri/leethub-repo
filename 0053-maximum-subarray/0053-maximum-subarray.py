class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        
        for each in nums:
            if currSum < 0:
                currSum = 0
            currSum += each
            maxSub = max(maxSub, currSum)
            
        return maxSub