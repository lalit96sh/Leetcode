class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        n = len(arr)
        ans = 0
        arr.sort()
        mod = ((10**9)+7)
        def twosum(start,target):
            
            end = n-1
            nonlocal ans
            while start<end:
                if arr[start]+arr[end]==target:
                    if arr[start]!=arr[end]:
                        start+=1
                        end-=1
                        st=1
                        ed = 1

                        while start<=end and arr[start]==arr[start-1]:
                            st+=1
                            start+=1
                        while start<=end and arr[end]==arr[end+1]:
                            ed+=1
                            end-=1

                        ans+=(st*ed)%mod
                    else:
                        ln = end-start+1
                        ans+=((ln*(ln-1))//2)
                        ans%=mod
                        break
                    
                elif arr[start]+arr[end]<target:
                    start+=1
                else:
                    end-=1
                    
        for start in range(n-2):
            
            twosum(start+1,target-arr[start])
            
            
        return ans
                    
            
        