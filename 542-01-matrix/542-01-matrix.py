class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    mat[i][j] = float("inf")
                    
        
        for i in range(m):
            for j in range(n):
                # if mat[i][j] == 0:
                #     dis[i][j] = 0
                #     continue
                
                if i>0:
                    mat[i][j] = min(mat[i][j],1+mat[i-1][j])
                if j>0:
                    mat[i][j] = min(mat[i][j],1+mat[i][j-1])
                    
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i<m-1:
                    mat[i][j] = min(mat[i][j],1+mat[i+1][j])
                if j<n-1:
                    mat[i][j] = min(mat[i][j],1+mat[i][j+1])
                    
        return mat