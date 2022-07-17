# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.node = root
        self.st = []        

    def next(self) -> int:
        cur = self.node
        while cur:
            self.st.append(cur)
            cur = cur.left
        
        new_node = self.st.pop()
        
        self.node = new_node.right
        
        return new_node.val
        

    def hasNext(self) -> bool:
        return self.node or self.st


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()