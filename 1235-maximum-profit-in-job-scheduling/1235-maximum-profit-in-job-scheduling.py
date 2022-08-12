class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
            
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        
        def find_index(val):
            l = 0
            r = len(dp)-1
            
            while l<r:
                mid = (l+r+1)//2
                
                if dp[mid][0]<=val:
                    l = mid
                else:
                    r = mid-1
                    
            return l
            
            
        for s, e, p in jobs:
            i = find_index(s)

            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
        
        
            
            