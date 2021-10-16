class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        l, r = 0, 0
        
        while r < len(nums)-1:
            temp = 0
            for i in range(l, r+1):
                temp = max(temp, i+nums[i])
            l = r+1
            r = temp
            ret += 1
        return ret
        