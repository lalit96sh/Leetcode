class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        st = []
        
#         for i,h in enumerate(heights):
#             while st and heights[st[-1]]<=h:
#                 st.pop()
#             st.append(i)
        
#         return st
        n = len(heights)
        mx = float("-inf")
        for i in range(n-1,-1,-1):
            if heights[i]<=mx:
                continue
            
            st.append(i)
            mx = heights[i]
            
        return st[::-1]
            