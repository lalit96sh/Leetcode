class Solution:
    def calculate(self, s: str) -> int:
        
        st = []
        cur_digit = 0
        ans = 0
        sign = 1
        
        
        for ch in s:
            
            if ch.isnumeric():
                cur_digit = (10*cur_digit)+int(ch)
                
            elif ch in ["+","-"]:
                
                ans += (sign*cur_digit)
                
                cur_digit = 0
                sign = 1 if ch=="+" else -1
            
            elif ch == "(":
                
                st.append(ans)
                st.append(sign)
                
                ans=0
                sign = 1
                
            elif ch==")":
                
                ans+=(sign*cur_digit)
                
                old_sign = st.pop()
                old_ans = st.pop()
                
                ans = old_ans+(old_sign*ans)
                
                sign = 1
                cur_digit =0
                
        return ans+(sign*cur_digit)