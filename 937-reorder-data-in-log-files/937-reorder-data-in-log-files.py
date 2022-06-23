class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_representation(log):
            
            _id,content = log.split(" ",maxsplit=1)
            
            return (0,content,_id) if content[0].isalpha() else (1,)
        
        return sorted(logs,key = get_representation)