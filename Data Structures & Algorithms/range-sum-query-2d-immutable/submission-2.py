class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if matrix:
            self.prefix = [[0]*(len(matrix[0])) for _ in range(len(matrix)+1)]
            for R in range(1,len(matrix)+1):
                total = 0
                for C in range(len(matrix[R-1])):
                    total += matrix[R-1][C]
                    self.prefix[R][C] = total + self.prefix[R-1][C]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomR = self.prefix[row2+1][col2]
        above = self.prefix[row1][col2]
        left = self.prefix[row2+1][col1-1] if col1 > 0 else 0
        upperL = self.prefix[row1][col1-1] if col1 > 0 else 0
        return (bottomR - above -left + upperL)


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)