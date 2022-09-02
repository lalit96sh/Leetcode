class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
            
        st = [float("inf")]
        
        res = 0
        
        for num in arr:
            
            while st and st[-1]<=num:
                val = st.pop()
                
                res+=val*min(st[-1],num)
            
            st.append(num)
            
        while len(st)>2:
            val = st.pop()
            res+=val*st[-1]
        return res
                
            
            
            