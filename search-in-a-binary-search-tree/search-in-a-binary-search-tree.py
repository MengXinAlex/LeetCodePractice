# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(n):
            if not n:
                return
            if n.val == val:
                return n
            if n.val > val:
                return search(n.left)
            else:
                return search(n.right)
            
        return search(root)