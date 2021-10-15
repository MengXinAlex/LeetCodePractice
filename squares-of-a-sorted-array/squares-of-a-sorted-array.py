class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        while left<len(nums)-2 and abs(nums[left])>=abs(nums[left+1]):
            left += 1
        right = left+1
        print(left)
        
        ret = []
        
        for i in range(len(nums)):
            if left < 0:
                pass
            elif right == len(nums) or abs(nums[right]) > abs(nums[left]):
                ret.append(nums[left]**2)
                left -= 1
                continue
            ret.append(nums[right]**2)
            right += 1
        return ret
              