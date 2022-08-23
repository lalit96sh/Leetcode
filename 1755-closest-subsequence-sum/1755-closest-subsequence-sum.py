class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        
        sum1 = set()
        sum2 = set()
        
        def dfs(start,end,cursum,_set):
            if start>end+1:
                return
            if start==end+1:
                _set.add(cursum)
                return
            
            dfs(start+1,end,cursum,_set)
            dfs(start+1,end,cursum+nums[start],_set)
            
        
        n = len(nums)
        
        dfs(0,(n//2)-1,0,sum1)
        dfs(n//2,n-1,0,sum2)
        
        sum2 = sorted(sum2)
        
        ans = float("inf")
        for s in sum1:
            
            remain = goal-s
            
            idx = bisect.bisect_left(sum2,remain)
            
            if idx<len(sum2):
                ans = min(ans,abs(remain-sum2[idx]))
            if idx>0:
                ans = min(ans,abs(remain-sum2[idx-1]))
            
        return ans
        
			# # sort the possible sums of the 2nd half
			# s2=sorted(sum2)
			# ans=10**10
			# # for each possible sum of the 1st half, find the sum in the 2nd half
			# # that gives a value closest to the goal using binary search
			# for s in sum1:
			# remain=goal-s
			# # binary search for the value in s2 that's closest to the remaining value
			# i2=bisect_left(s2,remain)
			# if i2<len(s2):
			# ans=min(ans,abs(remain-s2[i2]))
			# if i2>0:
			# ans=min(ans,abs(remain-s2[i2-1]))
			# return ans
                
            
            
            
            
        
        