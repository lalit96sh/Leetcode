# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        
        def dfs(root,cur,sm):
            
            if not root:
                return
            
            if (not root.left) and (not root.right) and sm+root.val==targetSum:
                ans.append(list(cur)+[root.val])
            
            cur.append(root.val)
            dfs(root.left,cur,sm+root.val)
            dfs(root.right,cur,sm+root.val)
            cur.pop()
            
            
        dfs(root,[],0)
        return ans
        