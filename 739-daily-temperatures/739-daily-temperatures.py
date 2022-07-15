class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        st = []
        ans = [0]*n
        
        for i in range(n):
            
            while st and temperatures[st[-1]]<temperatures[i]:
                j = st.pop()
                ans[j] = i-j
            st.append(i)
        
        return ans
        