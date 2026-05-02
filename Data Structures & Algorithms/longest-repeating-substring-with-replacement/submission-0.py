class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, length = 0, 0
        window = {}
        for R in range(len(s)):
            if s[R] in window:
                window[s[R]] += 1
            else:
                window[s[R]] = 1
            while R - L + 1 - max(window.values()) > k:
                if s[L] in window:
                    window[s[L]] -= 1
                    if s[L] == 0:
                        window.pop(s[L])
                L += 1
            length = max(length, R - L + 1)
        return length
                

        
        