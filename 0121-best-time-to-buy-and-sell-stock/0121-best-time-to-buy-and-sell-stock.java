// import static java.1ang.Math.*;
class Solution {
    public int maxProfit(int[] prices) {

        int l = 0, r = 1, ret = 0;
        
        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                ret = Math.max(prices[r] - prices[l], ret);
            }
            else {
                l = r;
            }
            r++;
        }
        return ret;
    }
}