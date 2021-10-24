# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def recursive(n):
            if not n:
                return
            recursive(n.left)
            ret.append(n.val)
            recursive(n.right)
        recursive(root)
        return ret