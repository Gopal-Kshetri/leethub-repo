class Solution:
      keys = {
      '2': ['a','b','c'],
      '3': ['d','e','f'],
      '4': ['g','h','i'],
      '5': ['j','k','l'],
      '6': ['m','n','o'],
      '7': ['p','q','r', 's'],
      '8': ['t','u','v'],
      '9': ['w','x','y', 'z']
      }
      def letterCombinations(self, digits: str, combination = ""):
        output = []
        if(len(digits)==0):
          if(len(combination)!=0):
            output.append(combination)
        else:
          for letter in self.keys[digits[0]]:
            output += self.letterCombinations(
              digits[1:],
              combination + letter
            )
            
        return output