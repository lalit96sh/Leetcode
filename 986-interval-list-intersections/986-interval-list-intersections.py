class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i = 0
        j = 0
        
        if not firstList or not secondList:
            return []
        
        result = []
        
        firstList.sort()
        secondList.sort()
        
        while i<len(firstList) and j< len(secondList):
            
            s1,e1 = firstList[i]
            s2,e2 = secondList[j]
            
            if s1<=e2 and s2<=e1:
                result.append([max(s1,s2),min(e1,e2)])
                
            if e1<e2:
                i+=1
            else:
                j+=1
        
        return result
                
        