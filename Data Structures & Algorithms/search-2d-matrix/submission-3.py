class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        M, N = len(matrix), len(matrix[0])
        L, R = 0, M-1
        while L <= R:
            midR = (L+R)//2
            if target > matrix[midR][N-1]:
                L = midR+1
            elif target < matrix[midR][0]:
                R = midR-1
            else:
                break
        if target > matrix[midR][N-1] or target < matrix[midR][0]:
            return False
        L, R = 0, N-1
        while L <= R:
            midC = (L+R)//2
            if target > matrix[midR][midC]:
                L = midC+1
            elif target < matrix[midR][midC]:
                R = midC-1
            else:
                return True
        return False
        
        