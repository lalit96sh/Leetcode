class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if 2*k >= len(prices): 
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        dp = [0]*(k+1)
        mn = [prices[0]]*(k+1)
        
        n = len(prices)
        # print(mn)
        # print(dp)
        # print("--------------------")
        for i in range(1,n):
            for kk in range(1,k+1):
                if mn[kk]>prices[i]-dp[kk-1]:
                    mn[kk] = prices[i]-dp[kk-1]
                else:
                    dp[kk] = max(dp[kk],prices[i]-mn[kk])
                
        return dp[k]
            
        
        
        