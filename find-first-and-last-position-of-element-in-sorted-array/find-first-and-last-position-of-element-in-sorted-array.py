class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # setting left and right pointers
        left, right = 0, len(nums) - 1
        while left < right:
            # and the middle pointer
            mid = left + (right - left) // 2
            # capture an occurrence
            if nums[mid] == target:
                # here to check for all occurrences
                first = last = mid
                # by iterating to the left of mid value
                while 0 <= first and nums[first] == target:
                    first -= 1
                # and to the right
                while last < len(nums) and nums[last] == target:
                    last += 1
                return [first+1, last-1]
            # shift the pointers if the target is not reached yet
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # by now all three pointers should meet at the same value
        # meaning, if the target is present in the list it occurs only once (at pointer index)
        # thus check if the pointer is inbounds and its element is indeed the target
        if 0 <= left and left < len(nums) and nums[left] == target:
            return [left, left]
        # otherwise the target is not present in the list
        else:
            return [-1, -1]