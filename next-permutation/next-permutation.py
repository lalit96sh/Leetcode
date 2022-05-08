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
        left = i
        right = n-1
        while left<right:
            mid = (left+right+1)//2
            if nums[mid]>nums[i]:
                left=mid
            else:
                right = mid-1
        print(i,left,right,nums)
        nums[i],nums[left] = nums[left],nums[i]
        
        r(nums,i+1)
        