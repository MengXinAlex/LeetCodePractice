class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = collections.Counter(ransomNote)
        s2 = collections.Counter(magazine)
        
        for i in s1:
            if i not in s2 or s1[i] > s2[i]:
                print(i, s1[i], s2[i])
                return False
        return True
        