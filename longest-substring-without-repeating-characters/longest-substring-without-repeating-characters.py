class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j, ret = 0, 0, 0
        unique = set()
        while i < n and j < n:
            if s[j] in unique:
                unique.remove(s[i])
                i += 1
            else:
                unique.add(s[j])
                j += 1
                ret = max(ret, j-i)
        return ret