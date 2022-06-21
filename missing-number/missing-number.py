class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sm = sum(nums)
        sm_t = (n*(n+1))//2
        return sm_t-sm