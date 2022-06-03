class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def f(start,end,k):
            if start==end:
                return nums[start]
            pivot = end
            
            i = start
            j = start
            
            for j in range(start,end):
                if nums[j]<nums[pivot]:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
            
            nums[i],nums[pivot] = nums[pivot],nums[i]
            
            if i==k:
                return nums[i]
            if i>k:
                return f(start,i-1,k)
            else:
                return f(i+1,end,k)
        n = len(nums)   
        return f(0,n-1,n-k)
            
        