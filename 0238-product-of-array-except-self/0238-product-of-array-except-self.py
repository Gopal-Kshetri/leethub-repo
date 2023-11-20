class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []
        product = 1
        for each in nums:
            product *= each
            prefix.append(product)
        product = 1
        for each in nums[::-1]:
            product *= each
            postfix.append(product)
        postfix = postfix[::-1]
        
        for i in range(len(nums)):
            pre = 1 if i == 0 else prefix[i - 1]
            post = 1 if i == len(nums) - 1 else postfix[i + 1]
            result.append(pre * post)

        return result   
            
            