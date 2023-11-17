class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for each in nums:
            if each in numMap:
                return True
            numMap[each] = each
        return False