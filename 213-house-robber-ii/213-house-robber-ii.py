class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def func(start,end):
            last = nums[start]
            second_last = 0
            n = end
            for i in range(start+1,n):
                second_last, last = max(last,second_last), second_last+nums[i]
            return max(last,second_last)
        
        if len(nums)==1:
            return nums[0]
        
        x = len(nums)
        
        return max(func(0,x-1),func(1,x))
        
            