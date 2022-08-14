# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        st = []
        
        cur = root
        node_found = False
        while st or cur:
            
            while cur:
                st.append(cur)
                cur = cur.left
            node = st.pop()
            if node_found:
                return node
            
            if node==p:
                node_found = True
                
            cur = node.right
        
        return None
            
            
            
            
        
        