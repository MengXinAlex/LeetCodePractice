class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            ret = max(ret, cur)
        return ret
        