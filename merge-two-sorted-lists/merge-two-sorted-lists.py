# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if None Node
        if not l1:
            return l2
        if not l2:
            return l1
        
        ret = None
        
        # loop both ListNode
        while l1 and l2:
            
            if l1.val < l2.val:
                v = l1.val
                l1 = l1.next
            else:
                v = l2.val
                l2 = l2.next
                
            if not ret:
                ret = ListNode(v)
            else:
                temp = ret
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(v)
                
        # check whos left
        temp = ret
        while temp.next:
            temp = temp.next
            
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return ret
            
        