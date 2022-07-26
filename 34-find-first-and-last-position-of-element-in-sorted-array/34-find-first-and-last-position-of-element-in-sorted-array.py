class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        n = len(nums)
        
        l = 0
        r = n-1
        
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]>=target:
                r = mid
            else:
                l = mid+1
                
        
        if nums[l]!=target:
            return [-1,-1]
        
        ans = [l,l]
        
        r = n-1
        
        while l<r:
            
            mid = (l+r+1)//2
            
            if nums[mid]==target:
                l = mid
            else:
                r = mid-1
        
        ans[1] = l
        
        return ans
        