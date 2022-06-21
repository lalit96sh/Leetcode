class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left = [1]*n
        for i in range(1,n):
            left[i] = nums[i-1]*left[i-1]
        r = 1
        for i in range(n-1,-1,-1):
            left[i] = left[i]*r
            r = r*nums[i]
        return left
            