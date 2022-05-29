class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        
        c1 = None
        c2 = None
        
        cnt1 = 0
        cnt2 = 0
        
        for x in nums:
            if x==c1:
                cnt1+=1
            elif x==c2:
                cnt2+=1
            elif cnt1==0:
                cnt1+=1
                c1 = x
            elif cnt2==0:
                cnt2+=1
                c2=x
            else:
                cnt1-=1
                cnt2-=1
        r = []
        for c in [c1,c2]:
            if c is not None:
                if nums.count(c)>len(nums)//3:
                    r.append(c)
        return r