class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n==1:
            return 0
        
        mn = prices[0]
        
        ans = 0
        
        for i in range(1,n):
            
            if prices[i]<mn:
                mn = prices[i]
            else:
                ans = max(ans,prices[i]-mn)
        return ans
        
        