class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        if min(sr, sc) < 0 or sr >= row or sc >= col:
            return
        temp = image[sr][sc]
        if temp == color:
            return image
        image[sr][sc] = color
        if sr >= 1 and image[sr-1][sc] == temp:
            self.floodFill(image, sr-1, sc, color)
        if sr < row-1 and image[sr+1][sc] == temp:
            self.floodFill(image, sr+1, sc, color)
        if sc >= 1 and image[sr][sc-1] == temp:
            self.floodFill(image, sr, sc-1, color)
        if sc < col-1 and image[sr][sc+1] == temp:
            self.floodFill(image, sr, sc+1, color)
        return image
        
        


        