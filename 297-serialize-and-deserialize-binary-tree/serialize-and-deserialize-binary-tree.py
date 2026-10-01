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
        result = []
        def preorder(root):
            nonlocal result
            if not root:
                result.append("N")
                return
            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return "#".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        self.j = 0
        def dfs():
            if data[self.j] == "N":
                self.j += 2
                return None
            i = self.j
            while data[i] != "#":
                i += 1
            n = TreeNode(int(data[self.j:i]))
            self.j = i + 1
            n.left = dfs()
            n.right = dfs()
            return n
        return dfs()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))