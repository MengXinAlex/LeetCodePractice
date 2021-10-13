class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        cur = 0
        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            ret = max(ret, cur)
        return ret