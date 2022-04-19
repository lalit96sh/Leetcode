class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        
        if not matrix:
            return 0
        
        dp = [0] * (len(matrix[0])+1)
        maxLen = prev = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = dp[j+1]
                if matrix[i][j] == '1':
                    dp[j+1] = min(prev, dp[j], dp[j+1]) + 1
                    maxLen = max(maxLen, dp[j+1])
                else:
                    dp[j+1] = 0
                prev = temp        
        return maxLen * maxLen
                
                
                
        