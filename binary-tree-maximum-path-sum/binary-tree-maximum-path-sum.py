# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def f(root):
            if not root:
                return 0
            nonlocal ans
            leftgain = max(0,f(root.left))
            rightgain = max(0,f(root.right))
            
            ans = max(root.val+leftgain+rightgain,ans)
            
            
            
            return root.val+max(leftgain,rightgain)
        f(root)
        return ans
