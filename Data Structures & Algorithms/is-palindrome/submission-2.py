class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True;
        alpha_text = "".join(char for char in s if char.isalnum());
        clean_text = alpha_text.lower();
        for j in range(len(clean_text)//2):
            if clean_text[j] != clean_text[(len(clean_text)-1)-j]:
                result = False;
        return result;
