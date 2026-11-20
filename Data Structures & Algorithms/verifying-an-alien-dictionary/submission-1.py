class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        def check(w1, w2):
            def dfs(i):
                if len(w1)-1 < i and len(w2)-1 < i:
                    return True
                if len(w2)-1 < i:
                    return False
                if len(w1)-1 < i:
                    return True
                if order_index[w1[i]] > order_index[w2[i]]:
                    return False
                elif order_index[w1[i]] < order_index[w2[i]]:
                    return True
                else:
                    return dfs(i+1)
            return dfs(0)

        for i in range(1, len(words)):
            if not check(words[i-1], words[i]):
                return False
        return True
            
