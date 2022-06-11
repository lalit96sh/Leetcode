class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nm = set(nums)
        if not nums:
            return 0
        ans = 1
        
        i = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i]-1 in nm:
                continue
            cur = 1
            numb = nums[i]
            while numb+1 in nm:
                numb+=1
                cur+=1
            ans = max(ans,cur)

        return ans
            
        
        
        