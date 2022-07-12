class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        if target < nums[0]:
            return 0
        if target >nums[-1]:
            return n
        
        
        l,r = 0,n-1
        
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid]<target:
                l=mid+1
                
            else:
                r = mid
                
        return l
        