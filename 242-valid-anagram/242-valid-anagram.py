class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for i in s:
            if myDict.get(i):
                myDict[i] += 1
            else:
                myDict[i] = 1
        for i in t:
          if myDict.get(i) and myDict[i]>0:
            myDict[i] -= 1
          else:
            return False

        values = list(myDict.values())
        if values.count(0)!=len(values):
          return False
        
        return True