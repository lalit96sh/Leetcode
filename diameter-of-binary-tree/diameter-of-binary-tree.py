# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def f(node):
            if not node:
                return 0
            left = f(node.left)
            right = f(node.right)
            
            nonlocal ans
            ans = max(ans,1+left+right)
            
            return max(left,right)+1
        f(root)
        return ans-1
        