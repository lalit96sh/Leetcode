class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        mp = set()
        for i,_ in enumerate(emails):
            
            first,last = _.split("@")
            
            first = first.split("+")[0]
            
            first = first.replace(".","")
            
            mp.add("@".join([first,last]))
        
        return len(mp)