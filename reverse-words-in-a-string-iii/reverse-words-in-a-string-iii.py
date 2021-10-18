class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        temp = s.split()
        for i in temp:
            ret.append(i[::-1])
        return " ".join(str(i) for i in ret)