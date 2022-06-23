# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def f(root,mn=float("-inf"),mx=float("inf")):
            if not root:
                return True
            if root.val<=mn:
                return False
            if root.val>=mx:
                return False
            return f(root.left,mn,root.val) and f(root.right,root.val,mx)
        return f(root)