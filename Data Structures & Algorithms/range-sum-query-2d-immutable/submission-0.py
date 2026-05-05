class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if matrix:
            self.prefix = [[0]*len(matrix[0]) for _ in range(len(matrix))]
            for R in range(len(matrix)):
                total = 0
                for C in range(len(matrix[R])):
                    total += matrix[R][C]
                    self.prefix[R][C] = total        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for R in range(row1, row2+1):
            preL = self.prefix[R][col1 - 1] if col1 > 0 else 0
            total +=  self.prefix[R][col2] - preL  
        return total        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)