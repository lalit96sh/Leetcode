class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        
        mul = 1
        
        start=0
        n = len(nums)
        i=0
        ans = 0

        for i in range(n):
            mul*=nums[i]
            
            while start<=i and mul>=k:
                mul//=nums[start]
                start+=1
    
            ans+=i-start+1
        
        return ans
                
            
            
        