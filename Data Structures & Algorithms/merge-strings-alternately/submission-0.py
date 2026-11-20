class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        turn = True
        res = ""
        while i + j <= len(word1) + len(word2):
            if i >= len(word1):
                 res += word2[j:]
                 break
            if j >= len(word2):
                res += word1[i:]
                break
            if turn:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            turn = not turn
        return res

        