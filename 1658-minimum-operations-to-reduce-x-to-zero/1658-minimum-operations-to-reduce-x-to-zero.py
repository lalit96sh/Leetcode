class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        n = len(nums)
        j = 0
        
        total = sum(nums)
        cur = 0
        mx = -1
        for i,nm in enumerate(nums):
            
            cur+=nm
            
            while cur>total-x and j<=i:
                cur-=nums[j]
                j+=1
            
            if cur==total-x:
                mx = max(mx,i-j+1)
            
        return -1 if mx==-1 else n-mx
        
            
            
        