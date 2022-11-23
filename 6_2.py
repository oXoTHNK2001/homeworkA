#запускать через leetcode
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def checker_rob(nums):
            rob = 0
            not_rob = 0
            for num in nums:
                rob , not_rob = not_rob + num , max(rob,not_rob)
            return max(rob,not_rob)    
        if len(nums) == 1:
            return nums[-1]
        elif not nums:
            return 0
        else:
            return max(checker_rob(nums[1:]),checker_rob(nums[:-1]))