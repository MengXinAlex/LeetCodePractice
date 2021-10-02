# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        node = head
        temp = head
        
        while node.next:
            node = node.next
            if node.val == temp.val:
                temp.next = node.next
            else:
                temp = node
        return head