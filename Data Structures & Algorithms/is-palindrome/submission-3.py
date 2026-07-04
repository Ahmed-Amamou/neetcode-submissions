from string import ascii_lowercase

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics = ascii_lowercase + '0123456789'

        clean_string = ""
        for c in s:
            if c.lower() in alphanumerics:
                clean_string+=c.lower()
        
        left = 0
        right = len(clean_string) - 1
        while(left <= right):
            if clean_string[left] != clean_string[right]:
                return False
            
            left +=1
            right -=1
        
        return True
