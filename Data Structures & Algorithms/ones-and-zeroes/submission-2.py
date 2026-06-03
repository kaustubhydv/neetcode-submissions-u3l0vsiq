class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def dfs(i, currm, currn):
            if i >= len(strs):
                return 0
            if (i, currm, currn) in memo:
                return memo[(i, currm, currn)]
            res = dfs(i+1, currm, currn)
            zero = strs[i].count('0')
            one = strs[i].count('1')
            if zero <= currm and one <= currn:
                res = max(res, 1+dfs(i+1, currm-zero, currn-one))
            memo[(i, currm, currn)] = res
            return memo[(i, currm, currn)]
        return dfs(0, m, n)
