class Solution:
    def twoSum(self, nm: List[int], target: int) -> List[int]:
        
        nums = [(v,i) for i,v in enumerate(nm)]
        
        nums.sort()
        
        i = 0
        j = len(nums)-1
        
        while i<j:
            if nums[i][0]+nums[j][0]==target:
                return [nums[i][1],nums[j][1]]
            
            if nums[i][0]+nums[j][0]<target:
                i+=1
            else:
                j-=1
        return -1
        
        