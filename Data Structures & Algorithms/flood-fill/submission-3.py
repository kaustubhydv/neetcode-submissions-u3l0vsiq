class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        R, C = len(image), len(image[0])
        q = deque()
        ogColor = image[sr][sc]
        q.append((sr, sc))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                image[r][c] = color
                dirs = [[0,1], [0,-1], [1, 0], [-1,0]]
                for dr, dc in dirs:
                    newr = r+dr
                    newc = c+dc
                    if min(newr, newc) < 0 or newr >= R or newc >= C or image[newr][newc] != ogColor:
                        continue
                    else:
                        q.append((newr, newc))
        return image
        
        