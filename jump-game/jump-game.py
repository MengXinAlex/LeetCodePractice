class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        next = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > next:
                next = nums[i]
            next-=1 
            if next < 0:
                return False
        return next>=0
                
        