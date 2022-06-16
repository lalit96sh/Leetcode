class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        
        n = len(nums)
        memo = {}
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i]
            
        mx = [0]*n
        mx[n-1] = nums[n-1]
        for j in range(n-2,-1,-1):
            mx[j] = max(nums[j],mx[j+1])
        
        # @lru_cache
        def dfs(parts,index):
            if (parts,index) in memo:
                return memo[(parts,index)]
            if parts==1:
                return prefix[n-1] - prefix[index] + nums[index]
            if parts==n-index:
                return mx[index]
            
            mn = float("inf")
            cursum = 0
            
            for i in range(index,n-parts+1):
                cursum += nums[i]
                mn = min(mn,max(cursum,dfs(parts-1,i+1)))
                if mn<=cursum:
                    break
            memo[(parts,index)] = mn
            return mn
        
        return dfs(m,0)