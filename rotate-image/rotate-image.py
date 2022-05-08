class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        start = 0
        end = len(m)-1
        
        while start < end:
            
            for j in range(start,end):
                m[start][j] , m[end-(j-start)][start] = m[end-(j-start)][start], m[start][j]
                m[end-(j-start)][start], m[end][end-(j-start)] = m[end][end-(j-start)],m[end-(j-start)][start]
                m[end][end-(j-start)],m[j][end] = m[j][end],m[end][end-(j-start)]
            
            start+=1
            end-=1
        
        