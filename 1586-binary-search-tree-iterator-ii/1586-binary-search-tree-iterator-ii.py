# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.traversal,self.pointer = [],-1
        self.node = root
        
        

    def hasNext(self) -> bool:
        return bool(self.node or self.st or self.pointer<len(self.traversal)-1)

    def next(self) -> int:
        
        self.pointer+=1
        
        if self.pointer==len(self.traversal):
            
            while self.node:
                self.st.append(self.node)
                self.node=self.node.left
            
            self.node = self.st.pop()
            self.traversal.append(self.node)
            self.node = self.node.right

        return self.traversal[self.pointer].val

    def hasPrev(self) -> bool:
        return self.pointer>=1

    def prev(self) -> int:
        
        self.pointer-=1
        return self.traversal[self.pointer].val


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()