from collections import defaultdict

class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        dfdict = defaultdict(list)
        for i in a:
            sorted_i = " ".join(sorted(i))
            dfdict[sorted_i].append(i)
        return dfdict.values()