class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        ones = sum(data)
        n = len(data)
        start = 0
        cur_ones = max_ones = 0
        
        for i in range(n):
            
            cur_ones += data[i]
            
            if i-start+1>ones:
                cur_ones-=data[start]
                start+=1
                
            max_ones = max(max_ones,cur_ones)
        return ones-max_ones