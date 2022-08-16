class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [0]*n
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if matrix[i][j]=="0" else dp[j]+1
            
            st = [-1]
            dp.append(0)
            for k in range(n+1):
                while dp[st[-1]]>dp[k]:
                    height = dp[st.pop()]
                    width = k-st[-1]-1
                    ans = max(height*width,ans)
                st.append(k)
            dp.pop()
        return ans