class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[l]:
                r = mid
                
            elif nums[mid]>nums[r]:
                l = mid+1
            else :
                if nums[r-1]>nums[r]:
                    l = r
                r-=1
        return nums[l]