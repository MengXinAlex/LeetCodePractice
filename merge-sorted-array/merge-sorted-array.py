class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        for i in range(len(nums1)-1, -1, -1):
            if right < 0:
                pass
            elif left < 0 or nums2[right] >= nums1[left]:
                nums1[i] = nums2[right]
                right -= 1
                continue
            nums1[i] = nums1[left]
            left -= 1
        return nums1