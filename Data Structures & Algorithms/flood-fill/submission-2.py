class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        ogColor = image[sr][sc]
        if ogColor == color:
            return image
        def dfs(r, c):
            if r == ROW or c == COL or min(r, c) < 0 or image[r][c] != ogColor:
                return
            if image[r][c] == ogColor:
                image[r][c] = color
            dirs = [(0, 1), (1,0), (0, -1), (-1, 0)]
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        dfs(sr, sc)
        return image
        



        