class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        n = len(nums)
        count=0
        def f(start,cur):
            nonlocal count
            count+=1
            print(cur)
            r.append(cur)
            
            for i in range(start,n):
                f(i+1,cur+[nums[i]])
       
        f(0,[])
        print(count)
        return r
        