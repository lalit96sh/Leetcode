class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        
        def get_next(num,arr):
            
            ans = arr[0]
            
            for aa in arr:
                if aa>num:
                    return aa
            return ans
            
        def get_next_h2(num,arr):
            ans = arr[0]
            for aa in arr:
                if aa>num:
                    if aa>"3":
                        return ans,aa
                    return aa,aa
            return ans,ans
            
        nums = set()
        
        for t in time:
            if t==":":
                continue
            nums.add(t)
            
        
        nums = sorted(nums)
        h1 = [x for x in nums if "0"<=x<="2"]
        m1 = [x for x in nums if "0"<=x<="5"]
        
        mp = {
            4: nums,
            1: nums,
            3: m1,
            0: h1
        }
        
        rev = []
        for i in range(4,1,-1):
            if i==2:
                rev.append(":")
                continue
            n = get_next(time[i],mp[i])
            rev.append(n)
            if n>time[i]:
                return time[:i]+"".join(rev[::-1])
        
        
        valid_2_next,valid_next = get_next_h2(time[1],mp[1])
        if valid_next > time[1] and time[0]!="2":
            return time[0]+valid_next+"".join(rev[::-1])
        if valid_2_next > time[1] and time[0]=="2":
            return time[0]+valid_2_next+"".join(rev[::-1])
        
        n = get_next(time[0],mp[0])
        
        if n=="2":
            return n+valid_2_next+"".join(rev[::-1])
        return n+valid_next+"".join(rev[::-1])
        
                
        
        
            