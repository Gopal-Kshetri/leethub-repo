class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        # min_num = min(nums)
        for i in range(max(max_num, len(nums))+1):
            if i not in nums:
                return i