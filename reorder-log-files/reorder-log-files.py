class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from functools import cmp_to_key
        
        def identifier(log):
            return log.split()[0]
        
        def content(log):
            return " ".join(log.split()[1:])
            
        
        def type_log(log):
            return "dig" if log.split()[1].isnumeric() else "let"
        
        def comp(a,b):
            if type_log(a)==type_log(b):
                if type_log(a)=="dig":
                    return 0
                if content(a)==content(b):
                    return 1 if identifier(a)>identifier(b) else -1
                return 1 if content(a)>content(b) else -1
                
            elif type_log(a)=="let":
                return -1
            else:
                return 1
        
        return sorted(logs,key = cmp_to_key(comp))