class Solution {
    public int[] dailyTemperatures(int[] nums) {
        int n = nums.length, t = 0;
        int answer[] = new int[n];
        
        for (int i = n - 1; i >= 0; i--) {
            int temp = nums[i];
            if (temp >= t) {
                t = temp;
                continue;
            }
            int days = 1;
            while (nums[i + days] <= temp) {
                days += answer[i + days];
            }
            answer[i] = days;
        }
        return answer;
    }
}