class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode tail = head, pre = head, res = head;
        while (tail != null && tail.next != null) {
            res = tail.next;
            tail.next = res.next;
            res.next = pre;
            pre = res;
        }
        return res;
    }
}