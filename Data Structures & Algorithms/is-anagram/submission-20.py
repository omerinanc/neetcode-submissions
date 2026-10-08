class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False

        for x in s:
            for i in range(len(t)):
                if t[i] == x:
                    t = t[:i] + t[i+1:]
                    break              
            else:
                return False           

        return t == ""