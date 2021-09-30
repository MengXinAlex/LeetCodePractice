class Solution(object):
    
    def rec(self, nums, target, i, j):
        if j == 1:
            if target > nums[i]:
                return i+1
            else:
                return i
        else:
            if target < nums[i+j//2]:
                return self.rec(nums, target, i, j//2)
            elif target > nums[i+j//2]:
                return self.rec(nums, target, i+j//2,j - j//2)
            else:
                return i+j//2
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # use recursion to solve this
        return self.rec(nums, target, 0, len(nums))
        
        

        