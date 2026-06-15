class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        s2 = s[::-1]
        if (s == s2):
            return True
        else:
            return False