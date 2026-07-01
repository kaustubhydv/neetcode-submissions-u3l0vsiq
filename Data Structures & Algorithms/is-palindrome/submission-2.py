class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for ch in s:
            if ch.isalnum():
                st += ch.lower()
        rev = st[::-1]
        return st == rev

        
        