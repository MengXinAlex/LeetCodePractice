class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, ret = 0, 0
        for i in nums:
            temp = max(cur+i, ret)
            cur = ret
            ret = temp
        return ret