class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp problem
        dp = nums
        ret = dp[0]
        for i in range(1, len(nums)):
            if dp [i-1] > 0:
                dp[i] += dp[i-1]
            ret = max(ret, dp[i])
        return ret