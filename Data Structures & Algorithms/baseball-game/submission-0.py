class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i, val in enumerate(operations):
            if val == "+":
                ans.append(ans[-1] + ans[-2])
            elif val == "D":
                ans.append(ans[-1]*2)
            elif val == "C":
                ans.pop()
            else:
                ans.append(int(val))
        return sum(ans)
            

        