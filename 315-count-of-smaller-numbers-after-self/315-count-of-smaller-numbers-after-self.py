class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nm = [[v,i] for i,v in enumerate(nums)]
        
        ans = [0]*len(nums)

        def mergesort(left,right):
            if left>=right:
                return
            
            mid= left + (right-left)//2
            
            mergesort(left,mid)
            mergesort(mid+1,right)
            
            merge(left,right,mid+1)
            
        def merge(left,right,mid):
            
            i = left
            j = mid
            
            temp = []
            number_of_elemnts_smaller_than_left = 0
            
            
            while i < mid and j<=right:
                
                if nm[i][0]<=nm[j][0]:
                    ans[nm[i][1]] += number_of_elemnts_smaller_than_left
                    temp.append(nm[i])
                    i+=1
                else:
                    number_of_elemnts_smaller_than_left+=1
                    temp.append(nm[j])
                    j+=1
                    
            while i<mid:
                ans[nm[i][1]] += number_of_elemnts_smaller_than_left
                temp.append(nm[i])
                i+=1
            while j<=right:
                number_of_elemnts_smaller_than_left+=1
                temp.append(nm[j])
                j+=1
                
            for k in range(left,right+1):
                nm[k] = temp[k-left]
        
        mergesort(0,len(nm)-1)
        return ans
                
            
            