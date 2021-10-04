class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        num = str(n)
        while num not in sett:
            sett.add(num)
            sum = 0
            for i in num:
                sum += int(i)*int(i)
            if sum == 1:
                return True
            num = str(sum)
        return False   