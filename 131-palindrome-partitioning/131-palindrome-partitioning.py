class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        def is_pali(p):
            return p == p[::-1]
        def part(st,cur):
            if not st:
                result.append(cur)
                return
            for i,_ in enumerate(st):
                
                if is_pali(st[:i+1]):
                    part(st[i+1:],cur+[st[:i+1]])
        
        part(s,[])
        return result
            