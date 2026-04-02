class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = []
        for i in range(len(arr)-1):
            temp.append(max(arr[i+1:]))
        temp.append(-1)
        return temp
        