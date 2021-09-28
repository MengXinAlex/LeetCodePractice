# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return
        
        # find the list length
        list_length = 0
        temp = head
        while temp:
            list_length+=1
            temp = temp.next
        finding_length = list_length - n - 1
        
        # if delete the first element
        if finding_length == -1:
            return head.next
        
        # find the node
        temp = head
        for i in range(finding_length):
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        
        return head
            
            