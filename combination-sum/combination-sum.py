class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # using BackTracking (Brute Force)
        
        ret = []
        
        def backTracking(cur):
            if sum(cur) == target and sorted(cur) not in ret:
                ret.append(sorted(cur))
                return
            if sum(cur) > target:
                return
            for i in candidates:
                cur.append(i)
                backTracking(cur)
                cur.pop()
            return ret
        
        return backTracking([])