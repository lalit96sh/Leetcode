class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 0
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[k]:
                nums[k+1]=nums[i]
                k+=1
        return k+1
        