class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if 1 not in nums:
            return 1
        
        for i in range(n):
            if not (1<=nums[i]<=n):
                nums[i]=1
        # print(nums)
        for i in range(n):
            while nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        # print(nums)
        for i in range(n):
            # print(nums[nums[i]-1], nums[i])
            if nums[nums[i]-1] != i+1:
                return i+1
        return n+1
        