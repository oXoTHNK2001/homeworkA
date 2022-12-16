#запускать через leetcode
import sys
class Solution(object):
    def __init__(self):
        self.prev = sys.maxsize
        self.current_min = sys.maxsize
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        return self.current_min
        
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        self.current_min = min(self.current_min, abs(self.prev - node.val))
        self.prev = node.val
        self.inorder(node.right)