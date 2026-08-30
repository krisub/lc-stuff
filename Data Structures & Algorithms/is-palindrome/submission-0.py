class Solution:
    # isalnum
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ''

        for char in s:
            if char.isalnum():
                new_s += char.lower()

        j = len(new_s) - 1
        for i in range(0, len(new_s) // 2, 1):
            if new_s[i] != new_s[j]:
                return False
            j -= 1        

        return True