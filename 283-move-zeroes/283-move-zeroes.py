class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j]!=0:
                if i!=j:
                    nums[j],nums[i] = nums[i],nums[j]
                i+=1
        