class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            
            if nums[mid]>=target:
                right=mid
            else:
                left=mid+1
        if nums[left]!=target:
            return [-1,-1]
        r = []
        r.append(left)
        right = len(nums)-1
        
        while left<right:
            mid = (left+right+1)//2
            
            if nums[mid]==target:
                left=mid
            else:
                right=mid-1
        r.append(left)
        return r
        
        