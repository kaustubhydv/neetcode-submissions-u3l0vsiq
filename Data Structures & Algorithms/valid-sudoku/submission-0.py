class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            visit = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in visit:
                    return False
                else:
                    visit.add(board[r][c])
        
        for r in range(9):
            visit = set()
            for c in range(9):
                if board[c][r] == '.':
                    continue
                if board[c][r] in visit:
                    return False
                else:
                    visit.add(board[c][r])
        
        for sq in range(9):
            visit = set()
            for i in range(3):
                for j in range(3):
                    row = ((sq//3)*3 + i)
                    col = ((sq%3)*3 + j)
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in visit:
                        return False
                    else:
                        visit.add(board[row][col])
        return True


        

        
                


        