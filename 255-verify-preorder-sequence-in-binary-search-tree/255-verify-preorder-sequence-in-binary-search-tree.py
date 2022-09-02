class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        st = []
        mx_popped = float("-inf")
        for p in preorder:
           
            while st and st[-1]<p:
                popped = st.pop()
                if popped<=mx_popped:
                    return False
                mx_popped = max(mx_popped,popped)
                
            st.append(p)
        while st:
            popped = st.pop()
            if popped<=mx_popped:
                return False
            mx_popped = max(mx_popped,popped)
        
        return True
        