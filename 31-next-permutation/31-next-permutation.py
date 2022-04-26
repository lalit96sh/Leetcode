class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        def r(nums,start):
            end = n-1
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        while i >=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        if i<0:
            r(nums,0)
            return
        
        k = n-1
        while i<k:
            if nums[i]<nums[k]:
                break
            k-=1
        
        nums[i],nums[k] = nums[k],nums[i]
        
        r(nums,i+1)
        