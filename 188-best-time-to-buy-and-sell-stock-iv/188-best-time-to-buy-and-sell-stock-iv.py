class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        def get_profit_for_inf():
            last = float("inf")
            ans = 0
            for x in prices:
                ans+= max(0,x-last)
                last = x
            return ans
        
        n = len(prices)
        if 2*k>=n:
            return get_profit_for_inf()
        
        
        mn = [prices[0]]*(k+1)
        ans = [0]*(k+1)
        
        
            
        for val in prices[1:]:
            for kk in range(1,k+1):
                if val-ans[kk-1]<mn[kk]:
                    mn[kk] = val-ans[kk-1]
                else:
                    ans[kk] = max(ans[kk],val-mn[kk])
        return ans[k]
            
        
        
        