class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        @functools.lru_cache(None)
        def dfs(start,end):
            if start>end:
                return 0
            
            res = 0
            
            for i in range(start,end+1):
                
                val = nums[i]*nums[start-1]*nums[end+1]
                
                res = max(res,val+dfs(start,i-1)+dfs(i+1,end))
                
            return res
        return dfs(0,n-1)
                
                