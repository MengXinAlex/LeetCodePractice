class Solution {
    public int pivotIndex(int[] nums) {
        
        int start = 0, end = nums.length -1, count = 0;
        int sum = IntStream.of(nums).sum();
        
        for (int i = 0; i < nums.length; i++) {
            if (count == sum - nums[i]) return i;
            sum -= nums[i];
            count += nums[i];
        }
        
        return -1;
    }
}