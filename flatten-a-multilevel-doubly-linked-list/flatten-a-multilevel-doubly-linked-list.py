"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        ret = head
        n_list = []
        if ret.next:
            n_list.append(ret.next)
        if ret.child:
            n_list.append(ret.child)
        
        while n_list:
            node = n_list.pop()
            if node.next:
                n_list.append(node.next)
            if node.child:
                n_list.append(node.child)
            ret.next = node
            ret.child = None
            node.prev = ret
            ret = node
        return head
