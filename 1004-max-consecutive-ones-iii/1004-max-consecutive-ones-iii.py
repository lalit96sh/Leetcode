class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        ans = 0
        start = 0
        cnt=0
        for i,num in enumerate(nums):
            
            if num==0:
                cnt+=1
            
            if cnt>k:
                if nums[start]==0:
                    cnt-=1
                start+=1
            
        
        return i-start+1
            
        