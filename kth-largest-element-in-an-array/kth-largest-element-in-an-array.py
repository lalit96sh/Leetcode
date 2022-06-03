class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n-k
        def helper(start,end):
            if start==end:
                return nums[start]
            
            pivot = end
            
            j = start
            
            for i in range(start,end):
                if nums[i]<nums[pivot]:
                    nums[i],nums[j] = nums[j],nums[i]
                    j+=1
            
            nums[j],nums[pivot] = nums[pivot],nums[j]
            
            if j==k:
                return nums[j]
            
            if j<k:
                return helper(j+1,end)
            return helper(start,j-1)
        
        return helper(0,n-1)
            
            
        