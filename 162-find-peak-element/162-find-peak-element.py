class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def f(start,end):
            
            
            while start<end:
                mid = start+(end-start)//2
                
                left = nums[mid-1] if mid>0 else float("-inf")
                right = nums[mid+1] if mid<n-1 else float("-inf")
                
                if left<nums[mid]>right:
                    return mid
                if left<nums[mid]<right:
                    start=mid+1
                else:
                    end=mid-1
            return start
        return f(0,n-1)