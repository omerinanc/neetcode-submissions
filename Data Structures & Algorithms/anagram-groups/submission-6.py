class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while strs != []:
            innerGroup = []
            if len(strs) >= 1:
                innerGroup.append(strs[0])
                strs.pop(0)
            i=0
            while i < len(strs):
                if self.isAnagram(innerGroup[0], strs[i]):
                    innerGroup.append(strs[i])
                    strs.pop(i)
                    i-=1
                i+=1
            result.append(innerGroup)
        return result
                
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] < 0:
                return False

        return True