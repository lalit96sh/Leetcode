class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cur_string_index = 0
        cur_pattern_index = 0
        last_star = None
        n = len(s)
        while cur_string_index<n:
            
            if cur_pattern_index>=len(p) or (s[cur_string_index]!=p[cur_pattern_index] and p[cur_pattern_index] not in {"*","?"}):
                if last_star is None:
                    return False
                cur_pattern_index = last_star+1
                cur_string_index = last_star_compared+1
                last_star_compared = cur_string_index
            elif p[cur_pattern_index] == "*":
                last_star = cur_pattern_index
                cur_pattern_index+=1
                last_star_compared = cur_string_index
            else:
                cur_string_index+=1
                cur_pattern_index+=1
                
        while cur_pattern_index<len(p):
            if p[cur_pattern_index] != "*":
                return False
            cur_pattern_index+=1
        
        return True
                
            