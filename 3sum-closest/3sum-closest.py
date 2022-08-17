class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        required = target
        n = len(nums)
        k = 3
        
        def util(start,k,target):
            
            if k==2:
                l = start
                r = n-1
                diff = float("inf")
                while l<r:
                    cur_diff = target-(nums[l]+nums[r])
                    if cur_diff==0:
                        return 0
                    elif nums[l]+nums[r]<target:
                        l+=1
                    else:
                        r-=1
                    if abs(cur_diff)<abs(diff):
                        diff = cur_diff
                return diff
                
            else:
                diff = float("inf")
                for i in range(start,n-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    cur_diff = util(i+1,k-1,target-nums[i])
                    if cur_diff==0:
                        return 0
                    if abs(cur_diff)<abs(diff):
                        diff = cur_diff
                return diff
        
        ans = util(0,k,required)
                
                
        
        return target-ans