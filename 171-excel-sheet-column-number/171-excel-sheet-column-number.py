class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        v = 0
        
        for c in columnTitle:
            h = (ord(c)-ord("A"))+1
            v = (v*26)+h
        return v