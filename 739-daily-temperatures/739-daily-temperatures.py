class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        st = []
        ans = [0]*n
        
#         for i in range(n):
            
#             while st and temperatures[st[-1]]<temperatures[i]:
#                 j = st.pop()
#                 ans[j] = i-j
#             st.append(i)
        
#         return ans

        mx = 0
    
        for i in range(n-1,-1,-1):
            cur_temp = temperatures[i]
            
            if cur_temp>=mx:
                mx = cur_temp
                continue
            
            d = 1
            
            while temperatures[i+d]<=cur_temp:
                d+=ans[i+d]
            
            ans[i] = d
        return ans