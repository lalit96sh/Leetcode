class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m,n = len(image),len(image[0])
        
        def neighbours(i,j):
            
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = i+di,j+dj
                if 0<=x<m and 0<=y<n:
                    yield (x,y)
                
        cx = image[sr][sc]
        def dfs(i,j):
            
            if image[i][j]==color or image[i][j]!=cx:
                return
            image[i][j]=color
            for nx,ny in neighbours(i,j):
                dfs(nx,ny)
            
            
        dfs(sr,sc)
        return image
            
                
            
            
        
        