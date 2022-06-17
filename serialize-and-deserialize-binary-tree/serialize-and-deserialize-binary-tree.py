# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        q = [root]
        while q:
            node = q.pop(0)
            ans.append(str(node.val) if node else "None")
            if node:
                q.append(node.left)
                q.append(node.right)
        return ",".join(ans)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values = data.split(",")
        n = len(values)
        root = TreeNode(values[0])

        i = 1
        q = [root]
        
        while q:
            node = q.pop(0)
            
            if values[i]!="None":
                child = TreeNode(values[i])
                node.left = child
                q.append(child)
            i+=1
            if values[i]!="None":
                child = TreeNode(values[i])
                node.right = child
                q.append(child)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))