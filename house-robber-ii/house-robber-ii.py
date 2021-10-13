class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            ret, cur = 0, 0
            for i in nums:
                temp = max(cur+i, ret)
                cur = ret
                ret = temp
            return ret
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))