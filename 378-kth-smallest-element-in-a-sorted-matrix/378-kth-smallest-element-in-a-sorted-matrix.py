class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        def last_required(row,val):
            nums = matrix[row]
            l = 0
            r = n-1
            
            while l<r:
                mid = (l+r+1)//2
                
                if nums[mid]<=val:
                    l=mid
                else:
                    r=mid-1
            
            return l
        
        def enough(val):
            
            count, n = 0, len(matrix)
            row, col = n - 1, 0
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
            while row >= 0 and col < n:
                if matrix[row][col] > val:

                    # As matrix[row][col] is bigger than the mid, let's keep track of the
                    # smallest number greater than the mid
                    larger = min(larger, matrix[row][col])
                    row -= 1

                else:

                    # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                    # biggest number less than or equal to the mid

                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1

            return count, smaller, larger
        
        
        l =smaller = matrix[0][0]
        r = matrix[-1][-1]
        
        while l<r:
            
            mid = (l+r)//2
            
            count,smaller,larger = enough(mid)
            
            if count==k:
                return smaller
            
            if count<k:
                l = larger
            else:
                r = smaller
                
        return l
            
            
                
            
        