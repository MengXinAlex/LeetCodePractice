# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.pathSum(root,targetSum)
    
    def pathSum(self, node, targetSum):
        if not node.left and not node.right:
            if targetSum == node.val:
                return True
            else:
                return False
        T1, T2 = False, False
        if node.left:
            T1 = self.pathSum(node.left, targetSum-node.val)
        if node.right:
            T2 = self.pathSum(node.right, targetSum-node.val)
        return T1 or T2