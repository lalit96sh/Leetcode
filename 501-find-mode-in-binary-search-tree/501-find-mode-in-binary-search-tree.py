# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        
        node = root
        st = []
        if not root:
            return []
        prev = TreeNode("x")
        cur_count = 0
        ans = []
        mx = 0
        while node or st:
            
            while node:
                st.append(node)
                node=node.left
            
            new = st.pop()
            cur_count = 1 if prev.val!=new.val else cur_count+1
            if mx<cur_count:
                mx = cur_count
                ans = [new.val]
            elif mx==cur_count:
                ans.append(new.val)
                
                
            
            prev = new
            node = new.right
        
        return ans
            