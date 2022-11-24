class Solution:

  def threeSumClosest(self, s, target):
    s.sort()
    diff = float('inf')
    for k in range(len(s)):
      i, j = k + 1, len(s) - 1
      while i < j:
        sum_three = s[i] + s[j] + s[k]
        if abs(target - sum_three) < abs(diff):
          diff = target - sum_three
        if sum_three < target:
          i += 1
        else:
          j -= 1

      if diff == 0:
        break

    return target-diff