class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        st = []
        
        n = len(s)
        
        for i in range(n):
            
            if s[i]=="(":
                st.append("(")
            else:
                num = 0
                while st and type(st[-1])==type(1):
                    num+=st.pop()
                st.pop()
                
                st.append(2*num if num else 1)
        return sum(st)
                    
                    
        