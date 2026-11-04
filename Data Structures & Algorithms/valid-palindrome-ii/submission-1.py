class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 1
        def loop(L, R):
            nonlocal count
            while L <= R:
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                    continue
                count -= 1
                if count < 0:
                    return False
                return loop(L+1, R) or loop(L, R-1)
            return True
        return loop(0, len(s)-1)
        