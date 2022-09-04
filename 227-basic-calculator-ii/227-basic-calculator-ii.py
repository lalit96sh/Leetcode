class Solution:
    def calculate(self, s: str) -> int:
        l_s = 0
        l_si = 1
        
        c_s = 1
        c_si = 1
        
        n = len(s)
        st = []
        i = 0
        while i < n:
            
            c = s[i]
            
            if c.isdigit():
                
                num = 0
                while i<n and s[i].isdigit():
                    num = (10*num)+int(s[i])
                    i+=1
                
                c_s = c_s*num if c_si==1 else c_s//num
                continue
            elif c in ["*","/"]:
                
                c_si = 1 if c=="*" else -1
                
                
            elif c in ["+","-"]:
                
                l_s += (l_si*c_s)
                
                l_si = 1 if c=="+" else -1
                
                c_s = 1
                c_si = 1
                
            elif c=="(":
                
                st.append(l_s)
                st.append(l_si)
                
                st.append(c_s)
                st.append(c_si)
                
                l_s = 0
                l_si = 1
        
                c_s = 1
                c_si = 1
            
            elif c==")":
                num = l_s+(l_si*c_s)
                
                c_si = st.pop()
                c_s = st.pop()
                
                l_si = st.pop()
                l_s = st.pop()
                
                c_s = num*c_s if c_si==1 else num//c_s
                
                
            i+=1
        
        return l_s+(l_si*c_s)
                
                
                
                
                
                
            
                
        