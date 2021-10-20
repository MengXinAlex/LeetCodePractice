# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        v = []
        while head:
            v.append(head.val)
            head = head.next
        v.reverse()
        ret = ListNode()
        temp = ret
        for i in v:
            temp.next = ListNode(i)
            temp = temp.next
        return ret.next