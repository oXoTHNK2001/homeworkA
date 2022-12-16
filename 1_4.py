#запускать через leetcode
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x : x[0]-x[1])
        n = len(costs)//2
        out=0
        for i in costs:
            n-=1
            out+= i[1] if n < 0 else i[0]
        return out