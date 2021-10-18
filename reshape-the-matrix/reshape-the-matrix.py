class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        ret = []
        line = []
        count = 0
        for i in mat:
            for j in i:
                line.append(j)
                count += 1
                if count == c:
                    ret.append(line)
                    line = []
                    count = 0
        return ret
    