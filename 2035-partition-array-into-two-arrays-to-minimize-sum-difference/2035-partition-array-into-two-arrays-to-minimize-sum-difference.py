class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        sum1 = collections.defaultdict(set)
        sum2 = collections.defaultdict(set)
        
        
        
        def dfs(start,end,cursum,curlen,_sum):
            
            if start==end+1:
                _sum[curlen].add(cursum)
                return
            
            dfs(start+1,end,cursum,curlen,_sum)
            dfs(start+1,end,cursum+nums[start],curlen+1,_sum) 
            
        n = len(nums)

        dfs(0,(n//2)-1,0,0,sum1)
        dfs(n//2,n-1,0,0,sum2)
        
        # del sum2[0]
        # del sum1[0]
        
        goal = sum(nums)/2
        
        ans = float("inf")
        for l,left in sum1.items():
            
            r = (n//2)-l
            
            right = sorted(sum2[r])
            
            for s in left:
                remain = goal-s
                
                idx = bisect.bisect_left(right,remain)
                
                if idx<len(right):
                    ans = min(ans,abs(remain-right[idx]))
                    
                if idx>0:
                    ans = min(ans,abs(remain-right[idx-1]))
        
        return int(2*abs(ans))
            
            
                
 
        
            
        