#https://github.com/oXoTHNK2001/ALgoRhytm.git
#запускать через leetcode
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] > 0:
                    matrix[i][j] = 1+min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
        s = 0
        for el in matrix:
            s += sum(el)
        return s
