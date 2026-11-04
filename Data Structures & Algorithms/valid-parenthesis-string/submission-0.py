class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        char = []
        for i in range(len(s)):
            if s[i] == ')':
                if not star and not char:
                    return False
                if char:
                    char.pop()
                else:
                    star.pop()
            elif s[i] == '(':
                char.append(i)
            else:
                star.append(i)
        while star and char:
            if char.pop() > star.pop():
                return False
        return not char
        
            

        