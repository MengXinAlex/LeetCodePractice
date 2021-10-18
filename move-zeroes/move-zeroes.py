class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # for i in nums:
        #     if(i==0):
        #         nums.remove(i)
        #         nums.insert(len(nums),0)
        
        i, j, n = 0, 0, len(nums)
        
        while i < n:
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1
            