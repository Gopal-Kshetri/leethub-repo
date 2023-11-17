class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)
    # Building a hash table
    for i in range(n):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []