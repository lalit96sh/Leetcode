class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
#         nm = [(m,i) for i,m  in enumerate(nums)]
        
#         nm.sort()
#         mn = float("inf")
#         ans = 0
#         for val,index in nm:
#             if mn>index:
#                 mn = index
#             else:
#                 ans = max(index-mn,ans)
                
#         return ans
        n = len(nums)
        st = []
        for i,nm in enumerate(nums):
            if not st or nums[st[-1]]>nm:
                st.append(i)
        ans = 0
        for i in range(n-1,-1,-1):
            
            while st and nums[i]>=nums[st[-1]]:
                ans = max(ans,i-st.pop())
        
        return ans
                