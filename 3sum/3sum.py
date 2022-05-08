class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        if len(nums)<3 or nums[0]*3 > 0 or nums[n-1]<0:
            return []
        ans = []
        for k in range(n-1,1,-1):
            if k<n-1 and nums[k]==nums[k+1]:
                continue
            kval = nums[k]
            i = 0
            j = k-1
            while i<j:
                if nums[i]+nums[j]+kval == 0:
                    ans.append([nums[i],nums[j],kval])
                    i+=1
                    j-=1
                    while i<n and nums[i]==nums[i-1]:
                        i+=1
                        
                elif nums[i]+nums[j]+kval> 0:
                    j-=1
                else:
                    i+=1
        return ans
                    