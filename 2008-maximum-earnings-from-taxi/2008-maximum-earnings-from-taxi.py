class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        dp = [[0,0]]
        
        rides.sort(key=lambda x:x[1])
        
        for s,e,t in rides:
            index = bisect.bisect(dp,[s+1])-1
            
            if dp[index][1]+(e-s+t)>dp[-1][1]:
                dp.append([e,dp[index][1]+(e-s+t)])
                
        return dp[-1][1]
        