class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ret = 0
        min = 1
        for i in nums:
            ret += i
            if ret < min:
                min = ret
        if min < 0:
            return -min+1
        else: 
            return 1