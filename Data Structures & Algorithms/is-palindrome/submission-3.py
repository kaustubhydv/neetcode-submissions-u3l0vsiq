class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        string = ""
        for ch in s:
            no = ord(ch)
            if ord('A') <= no <= ord('Z') or ord('a') <= no <= ord('z') or ord('0') <= no <= ord('9') :
                string += ch
        L, R = 0, len(string) - 1
        while L < R:
            if string[L] != string[R]:
                return False
            L += 1
            R -= 1
        return True   

        