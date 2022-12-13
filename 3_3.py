#запускать с помошью leetcode
class Solution:
    def averageOfLevels(self, root):
        A = defaultdict(int  )
        N = defaultdict(float)
        def dfs(n,d):
            if n:
                A[d] += n.val
                N[d] += 1
                dfs(n.left ,d+1)
                dfs(n.right,d+1)
        dfs(root,0)
        return [ A[i]/N[i] for i in range(len(A)) ]