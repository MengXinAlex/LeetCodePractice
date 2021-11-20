import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        int[] new_nums = new int[n+1];
        for (int num : nums) {
            new_nums[num] = 1;
        }
        List<Integer> ret = new ArrayList<>(n);
        for (int i = 1; i <= n; i++) {
            if (new_nums[i] == 0) {
                ret.add(i);
            }
        }
        return ret;
    }
}