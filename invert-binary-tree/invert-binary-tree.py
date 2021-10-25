# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(curr: TreeNode):
            if curr:
                invert(curr.left)
                invert(curr.right)
                curr.left, curr.right = curr.right, curr.left
            return curr
        
        return invert(root) 