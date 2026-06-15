class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_list = list(t)
        count = 0

        for ch in s:
            try:
                idx = t_list.index(ch)
            except ValueError:
                return False
            t_list.pop(idx)
            count = count + 1

        return count == len(s)