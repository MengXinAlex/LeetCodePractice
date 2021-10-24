# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def recursive(root):
            if not root:
                return 
            ret.append(root.val)
            recursive(root.left)
            recursive(root.right)
        recursive(root)
        return ret