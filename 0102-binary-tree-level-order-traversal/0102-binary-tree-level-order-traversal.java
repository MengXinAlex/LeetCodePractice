/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null) return ret;
        List<TreeNode> mainQueue = new LinkedList<TreeNode>();
        mainQueue.add(root);
        while(!mainQueue.isEmpty()) {
            List<Integer>levelRet = new ArrayList<Integer>();
            List<TreeNode> levelQueue = new LinkedList<TreeNode>();
            for (TreeNode i : mainQueue) {
                levelRet.add(i.val);
                if (i.left != null) levelQueue.add(i.left);
                if (i.right != null) levelQueue.add(i.right);
            }
            ret.add(levelRet);
            mainQueue = levelQueue;
        }
        return ret;
        
    }
}