#запускать с помошью leetcode
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ''
        while head:
            num += str(head.val)
            head = head.next
        return int(num, base=2)