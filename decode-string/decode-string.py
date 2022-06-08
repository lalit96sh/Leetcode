class Solution:
    def decodeString(self, s: str) -> str:
        s+="]"
        n = len(s)
        def is_int(st):
            return "0"<=st<="9"
        
        i = 0
        def f(times=1):
            nonlocal i
            if i==n:
                return ""
            
            cur = ""
            last_time = 0
            while i<n:
                # print(i,s[i])
                if is_int(s[i]):
                    while is_int(s[i]):
                        last_time = (last_time*10) + int(s[i])
                        i+=1
                elif s[i]=="]":
                    i+=1
                    break
                elif s[i]=="[":
                    i+=1
                    cur += f(last_time)
                    last_time = 0
                else:
                    cur+=s[i]
                    i+=1
            # print("returning {}".format(cur*times))
            return cur*times
        return f()
            
        