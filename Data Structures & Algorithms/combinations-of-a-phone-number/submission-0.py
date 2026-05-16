class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        subset = []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i):
            if len(digits) == len(subset):
                res.append(subset.copy())
            if i >= len(digits):
                return
            val = digitToChar[digits[i]]
            for char in val:
                subset.append(char)
                dfs(i+1)
                subset.pop()

        if digits:
            dfs(0)
            for i in range(len(res)):
                res[i] = ''.join(res[i])
            return res
        else:
            return []

        