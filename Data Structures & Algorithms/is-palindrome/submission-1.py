class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        def alpN(char):
            return (ord('A') <= ord(char) <= ord('Z')
            or ord('a') <= ord(char) <= ord('z')
            or ord('0') <= ord(char) <= ord('9'))
        while L < R:
            if s[L] and not alpN(s[L]):
                L += 1
                continue
            if s[R] and not alpN(s[R]):
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

        