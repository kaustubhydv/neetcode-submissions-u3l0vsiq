class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        pare = []
        for ch in s:
            if ch in par:
                if pare and par[ch] == pare[-1]:
                    pare.pop()
                else:
                    return False
            else:
                pare.append(ch)
        return True if len(pare) == 0 else False

        

        