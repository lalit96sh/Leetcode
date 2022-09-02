class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        st = []
        
        for i,h in enumerate(heights):
            while st and heights[st[-1]]<=h:
                st.pop()
            st.append(i)
        
        return st