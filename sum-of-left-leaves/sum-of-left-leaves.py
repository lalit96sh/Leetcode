# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root):
            
            if not root:
                return 0,0
            l,ls = dfs(root.left)
            r,rs = dfs(root.right)
            # print("----")
            # print(root.val)
            # print(l,ls,r,rs)
            sm = 0
            if l==0 and r==0:
                # print(1,root.val)
                return 1,root.val
            
            # if l==1:
            sm+=ls
            if r>1:
                sm+=rs
            # print(1+max(l,r),sm)
            return 1+max(l,r),sm
        
        _,ans = dfs(root)
        return ans if _>1 else 0
            
            