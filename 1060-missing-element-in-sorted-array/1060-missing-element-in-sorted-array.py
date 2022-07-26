class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)
        
        l = 0
        r = n-1
        
        while l<r:
            
            mid = (l+r+1)//2
            
            if nums[mid]-mid-nums[0] <= k-1:
                l = mid
                
            else:
                r = mid-1
        
        diff =  nums[l]-nums[0]-l
        
        return nums[0]+k+l