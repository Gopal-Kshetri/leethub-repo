class Solution:

  def maxArea(self, height) -> int:
    max_amt = 0
    start = 0
    end = len(height) - 1
    while start<end:
        length = end - start
        max_amt = max(max_amt, min(height[start], height[end])* length)
        if(height[start]<=height[end]):
            start+=1
        else:
            end-=1

    return max_amt