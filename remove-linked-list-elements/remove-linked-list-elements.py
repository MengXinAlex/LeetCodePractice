# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return
        cur = head
        nxt = head.next
        while nxt:
            if nxt.val == val:
                cur.next = nxt.next
                nxt = cur.next
            else:
                cur = nxt
                nxt = nxt.next
        return head