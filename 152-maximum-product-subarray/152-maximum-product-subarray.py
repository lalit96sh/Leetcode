class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curmx = ans = mn = nums[0]
        n = len(nums)
        for i in range(1,n):
            temp = curmx
            curmx = max(nums[i],nums[i]*curmx,nums[i]*mn)
            
            mn = min(nums[i],mn*nums[i],temp*nums[i])
            
            ans = max(ans,curmx)
        return ans
            