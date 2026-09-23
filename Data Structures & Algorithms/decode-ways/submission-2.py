class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i, cache):
            if i >= len(s):
                return 1
            if i in cache:
                return cache[i]
            #Case-1
            if s[i] == '0':
                decode1 = 0
            else:
                decode1 = dfs(i+1, cache)
            #Case-2
            if i+1 >= len(s):
                cache[i] = decode1
                return cache[i]
            if s[i] == '0' or int(s[i:i+2]) > 26:
                decode2 = 0
            else:
                decode2 = dfs(i+2, cache)
            cache[i] = decode1 + decode2
            return cache[i]
        return dfs(0, {})

            

        