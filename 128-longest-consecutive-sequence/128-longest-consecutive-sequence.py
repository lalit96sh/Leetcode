class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nm = set(nums)
        ans = 0
        for x in nm:
            if x-1 not in nm:
                y = x+1
                l = 1
                while y in nm:
                    l+=1
                    y+=1
                ans = max(ans,l)
        return ans
#         mx = 0
#         mp = {}
#         for num in nums:
#             if num in mp:
#                 continue
#             left_i = num-1
#             left = 0
#             while left_i in mp:
#                 left+=1
#                 left_i-=1
#             right_i = num+1
#             right = 0
#             while right_i in mp:
#                 left+=1
#                 right_i+=1
 
#             mp[num] = left+right+1
#             mx = max(mx,mp[num])
#         return mx            
        