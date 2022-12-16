#запускать через leetcode
class Solution:
    def tribonacci(self, n):
        if n < 2: return n
        a, b, c = 0, 0, 1
        for n in range(2, n+1): c, b, a = a + b + c, c, b
        return c