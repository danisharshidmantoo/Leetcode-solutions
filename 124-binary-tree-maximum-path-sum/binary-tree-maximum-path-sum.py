# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.result = float('-inf')
        def helper(root):
            if not root:
                return 0
           
          
            l = helper(root.left)
            
            r = helper(root.right)
            self.result = max(self.result,l+root.val,r+root.val,l+r+root.val,root.val)
            return max(root.val,root.val + max(l,r))
        helper(root)
        return self.result