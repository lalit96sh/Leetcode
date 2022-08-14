class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        ans = 0
        start = 0
        cnt=0
        for i,num in enumerate(nums):
            
            if num==0:
                cnt+=1
            
            while cnt>k:
                if nums[start]==0:
                    cnt-=1
                start+=1
            
            ans = max(ans,i-start+1)
        
        return ans
            
        