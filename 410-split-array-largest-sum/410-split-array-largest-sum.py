class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
#         n = len(nums)
#         memo = {}
#         @lru_cache
#         def dfs(parts,index):
#             # if (parts,index) in memo:
#             #     return memo[(parts,index)]
#             if parts==1:
#                 return sum(nums[index:])
#             if parts==n-index:
#                 return max(nums[index:])
            
#             mn = float("inf")
#             cursum = 0
            
#             for i in range(index,n-parts+1):
#                 cursum += nums[i]
#                 mn = min(mn,max(cursum,dfs(parts-1,i+1)))
#             # memo[(parts,index)] = mn
#             return mn
        
#         return dfs(m,0)
    # class Solution:
    # def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        n = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            
            m_now = 1
            now_sum = 0
            for num in nums:
                now_sum+=num
                if now_sum>mid:
                    m_now+=1
                    now_sum = num
                    
            if m_now <= m:
                right = mid
            else:
                left = mid + 1
        
        return left