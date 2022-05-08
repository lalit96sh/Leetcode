class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        mp = set()
        for i,_ in enumerate(emails):
            
            first,last = _.split("@")
            
            first = first.replace(".","")
            
            first = first.split("+")[0]
            
            mp.add("@".join([first,last]))
        
        return len(mp)