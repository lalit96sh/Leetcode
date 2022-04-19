class Solution:
    def rob(self, nums: List[int]) -> int:
        
        last = nums[0]
        second_last = 0
        n = len(nums)
        for i in range(1,n):
            second_last, last = max(last,second_last), second_last+nums[i]
        return max(last,second_last)
        