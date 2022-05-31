class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        r = [nums[0]]
        
        for nm in nums[1:]:
            if nm>r[-1]:
                r.append(nm)
            else:
                left = 0
                end = len(r)-1
                while left < end:
                    mid = (left+end)//2
                    if r[mid]==nm:
                        left = mid
                        break
                    elif r[mid]<nm:
                        left = mid+1
                    else:
                        end=mid
                r[left] = nm 
        return len(r)