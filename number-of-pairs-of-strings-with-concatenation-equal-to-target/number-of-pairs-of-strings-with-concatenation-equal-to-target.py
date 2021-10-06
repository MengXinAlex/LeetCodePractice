class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ret = 0
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if target == nums[i] + nums[j] and i != j:
                    ret+=1
        return ret