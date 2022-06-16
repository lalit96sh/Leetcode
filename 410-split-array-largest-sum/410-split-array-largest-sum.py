class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
#         n = len(nums)
#         memo = {}
#         @lru_cache
#         def dfs(parts,index):
#             # if (parts,index) in memo:
#             #     return memo[(parts,index)]
#             if parts==1:
#                 return sum(nums[index:])
#             if parts==n-index:
#                 return max(nums[index:])
            
#             mn = float("inf")
#             cursum = 0
            
#             for i in range(index,n-parts+1):
#                 cursum += nums[i]
#                 mn = min(mn,max(cursum,dfs(parts-1,i+1)))
#             # memo[(parts,index)] = mn
#             return mn
        
#         return dfs(m,0)
    # class Solution:
    # def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        
        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))
        
        @functools.lru_cache(None)
        def get_min_largest_split_sum(curr_index: int, subarray_count: int):
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]
        
            # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(first_split_sum, 
                                        get_min_largest_split_sum(i + 1, subarray_count - 1))

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                if first_split_sum >= minimum_largest_split_sum:
                    break
            
            return minimum_largest_split_sum
        
        return get_min_largest_split_sum(0, m)