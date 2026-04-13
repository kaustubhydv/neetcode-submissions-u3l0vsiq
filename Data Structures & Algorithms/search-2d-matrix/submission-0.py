class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for val in matrix:
            if val[0] <= target <= val[-1]:
                matrix = val
                L, R = 0, len(matrix) - 1
                while L<=R:
                    mid = (L+R)//2
                    if target < matrix[mid]:
                        R = mid - 1
                    elif target > matrix[mid]:
                        L = mid + 1
                    else:
                        return True
                return False
        else:
            return False
        