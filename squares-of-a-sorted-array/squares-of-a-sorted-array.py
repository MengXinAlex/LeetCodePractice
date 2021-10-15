class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            ret.append(i**2)
        return sorted(ret)