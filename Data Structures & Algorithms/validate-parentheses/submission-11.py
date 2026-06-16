class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "[", "{"]
        close = [")", "]", "}"]

        if len(s) % 2 == 1:
            return False

        if any(ch not in open and ch not in close for ch in s):
            return False

        s = list(s)

        while len(s) > 0:
            found = False

            for x in range(len(s) - 1):
                if s[x] == "(" and s[x + 1] == ")":
                    s.pop(x + 1)
                    s.pop(x)
                    found = True
                    break
                if s[x] == "[" and s[x + 1] == "]":
                    s.pop(x + 1)
                    s.pop(x)
                    found = True
                    break
                if s[x] == "{" and s[x + 1] == "}":
                    s.pop(x + 1)
                    s.pop(x)
                    found = True
                    break

            if not found:
                return False

        return True