class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        required = target
        ans = []
        n = len(nums)
        k = 4
        if nums[n-1]*k < required:
            return []
        
        def util(start,k,target,cur):
            if n-start<k or nums[start]*k>target:
                return
            
            if k==2:
                l = start
                r = n-1
                
                while l<r:
                    if nums[l]+nums[r]==target:
                        ans.append(cur+[nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif nums[l]+nums[r]<target:
                        l+=1
                    else:
                        r-=1
                
            else:
                
                for i in range(start,n):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    util(i+1,k-1,target-nums[i],cur+[nums[i]])
        
        util(0,k,required,[])
                
                
        
        return ans
                    