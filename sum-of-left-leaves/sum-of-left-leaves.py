# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def addOn(node, isLeft = False):
            nonlocal ret
            if not node:
                return
            if node.left:
                addOn(node.left, True)
            if node.right:
                addOn(node.right)
            if not node.right and not node.left and isLeft:
                ret += node.val
        addOn(root)
        return ret
                