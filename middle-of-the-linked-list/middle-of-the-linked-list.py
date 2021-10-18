# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp, ret = head, head
        c = 0
        while temp.next:
            temp = temp.next
            c+=1
        for i in range(0, (c+1)//2):
            ret = ret.next
        return ret
            
            