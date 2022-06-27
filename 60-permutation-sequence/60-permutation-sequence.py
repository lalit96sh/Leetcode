class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        numbers = [str(i) for i in range(1,n+1)]
        ans = ""
        k-=1
        while n>0:
            index,k = divmod(k,math.factorial(n-1))
            ans+=numbers[index]
            numbers.remove(numbers[index])
            n-=1
        return ans
        