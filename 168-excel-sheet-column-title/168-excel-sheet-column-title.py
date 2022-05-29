class Solution:
    def convertToTitle(self, c: int) -> str:
        s = ""
        while c:
            v = (c-1)%26
            s=chr(ord("A")+v)+s
            c = (c-1)//26
        return s
        