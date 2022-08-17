class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        i,ie = 0,m-1
        j,je = 0,n-1
        
        ans = []
        while i<=ie and j<=je:
            
            for x in range(j,je+1):
                ans.append(matrix[i][x])
                
            i+=1
            
            
            for x in range(i,ie+1):
                ans.append(matrix[x][je])
                
            je-=1
            
            if i<=ie:
                for x in range(je,j-1,-1):
                    ans.append(matrix[ie][x])

                ie-=1
            
            if j<=je:
                for x in range(ie,i-1,-1):
                    ans.append(matrix[x][j])

                j+=1
        return ans
                
            
            