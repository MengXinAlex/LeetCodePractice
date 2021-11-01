class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [1]
        index = 0
        while index != rowIndex:
            index += 1
            row = []
            for i in range(index):
                if i-1 >= 0:
                    row.append(ret[i-1] + ret[i])
                else:
                    row.append(ret[i])
            row.append(1)
            ret = row
            
            
        return ret
        