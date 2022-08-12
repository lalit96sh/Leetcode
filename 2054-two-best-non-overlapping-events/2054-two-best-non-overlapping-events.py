class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        jobs = sorted(events, key=lambda v: v[1])
        dp = [0]
        
        def find_index(val):
            l = 0
            r = len(dp)-1
            
            while l<r:
                mid = (l+r+1)//2
                
                if dp[mid]<=val:
                    l = mid
                else:
                    r = mid-1
                    
            return l
            
        mx = 0
        mp = {0:0}
        ans = 0
        for s, e, p in jobs:
            mx = max(mx,p)
            dp.append(e)
            mp[e] = mx
            i = find_index(s-1)
            ans = max(ans,p+mp[dp[i]])
        return ans
        