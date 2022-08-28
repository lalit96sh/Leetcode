class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        counter = Counter(nums)
        end = Counter()
                
        for num in nums:
            
            if not counter[num]:
                continue
                
            counter[num]-=1
            
            if end[num-1]>0:
                end[num-1]-=1
                end[num]+=1
            elif counter[num+1]>0 and counter[num+2]:
                counter[num+1]-=1
                counter[num+2]-=1
                end[num+2]+=1
            else:
                return False
        
        return True
                
            