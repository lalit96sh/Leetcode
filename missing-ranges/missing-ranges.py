class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def print(x,y):
            if x==y:
                return "{}".format(x)
            return "{}->{}".format(x,y)
        ans = []
        for nm in nums:
            if lower>upper:
                break
            if lower<nm:
                ans.append(print(lower,min(nm-1,upper)))
                lower=nm+1
            elif lower==nm:
                lower=nm+1
        if lower<=upper:
            ans.append(print(lower,upper))
        return ans 