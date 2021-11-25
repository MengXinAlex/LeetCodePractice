class Solution {
    public int maxSubArray(int[] nums) {
        int ret = nums[0];
        int cur = 0;
        for (int i : nums) {
            if (cur < 0) cur = 0;
            cur += i;
            ret = Math.max(ret, cur);
        }
            
        return ret;
    }
}