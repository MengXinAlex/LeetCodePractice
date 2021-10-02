# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        return self.findMD(root,depth)
        
        # recursion 
    
    def findMD(self, root, depth):
        if not root:
            return depth
        else:
            return max(self.findMD(root.left, depth+1), self.findMD(root.right, depth+1))