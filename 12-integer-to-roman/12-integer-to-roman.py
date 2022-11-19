class Solution:

  def intToRoman(self, num: int) -> str:
    myDict = {
      1000: "M",
      900: "CM",
      500: "D",
      400: "CD",
      100: "C",
      90: "XC",
      50: "L",
      40: "XL",
      10: "X",
      9: "IX",
      5: "V",
      4: "IV",
      1: "I"
    }
    result = ''
    # print(next(iter(myDict)))
    for i in range(13):
      val = list(myDict.keys())[i]
      while num >= val:
        result += myDict.get(val)
        num -= val

    return result