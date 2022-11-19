class Solution:

  def romanToInt(self, s: str) -> int:
    myDict = {
      "M": 1000,
      "D": 500,
      "C": 100,
      "L": 50,
      "X": 10,
      "V": 5,
      "I": 1,
    }
    val = []
    for i in s:
      val.append(myDict.get(i))
    val.append(0)
    result = 0
    i = 0
    while i < len(val) - 1:
      if val[i] < val[i + 1]:
        result += -val[i] + val[i + 1]
        i += 2
      else:
        result += val[i]
        i += 1

    return result