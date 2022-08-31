class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*n
        
        prefix[0] = nums[0]
        
        for i in range(1,n):
            prefix[i] = nums[i]+prefix[i-1]
            
        
        mp = collections.defaultdict(int)
        mp[k] = 1
        ans = 0
        for i in range(n):
            if prefix[i] in mp:
                ans+=mp[prefix[i]]
            mp[k+prefix[i]]+=1
        return ans
        