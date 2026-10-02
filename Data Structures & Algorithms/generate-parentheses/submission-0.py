class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        para = {
        "(" : n,
        ")" : n
        }
        def dfs(op, st):
            if para["("] == 0 and para[")"] == 0:
                res.append(st)
                return
            if op == 0:
                para["("] -= 1
                dfs(1, st+"(")
                para["("] += 1
            else:
                if para["("] == 0:
                    res.append(st + ")" * para[")"])
                    return
                else:
                    para["("] -= 1
                    dfs(op + 1, st+"(")
                    para["("] += 1
                    para[")"] -= 1
                    dfs(op - 1, st+")")
                    para[")"] += 1
            return
        dfs(0, "")
        return res


        