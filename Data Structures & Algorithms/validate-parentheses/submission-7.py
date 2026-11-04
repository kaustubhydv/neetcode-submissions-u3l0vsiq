class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        charT = []
        for ch in s:
            if ch not in par:
                charT.append(ch)
                continue
            if not charT or par[ch] != charT[-1]:
                return False
            charT.pop()
        return True if not charT else False
        