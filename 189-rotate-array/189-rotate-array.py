class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count=0
        i = 0
        while count<n:
            temp = nums[i]
            j = (i+k)%n
            while count<n:
                
                nums[j],temp = temp,nums[j]
                count+=1
                if i==j:
                    break
                j = (j+k)%n
            i+=1
                
            
            
        