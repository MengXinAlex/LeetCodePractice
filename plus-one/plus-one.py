class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                plus = 0
                break
        if plus:
            digits.insert(0,1)
        return digits
        