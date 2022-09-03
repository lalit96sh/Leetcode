class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        
        st = []
        
        for i,_str in enumerate(s):
            
            if _str==")":
                cur = ""
                while st and st[-1]!="(":
                    cur=st.pop()+cur

                if st and st[-1]=="(":
                    st.append(st.pop()+cur+")")
                elif cur:
                        st.append(cur)
            else:
                st.append(_str)
                
        return "".join(i for i in st if i!="(")
                
                
        