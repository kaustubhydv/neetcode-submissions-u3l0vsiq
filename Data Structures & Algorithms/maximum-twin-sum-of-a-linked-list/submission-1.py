# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev, curr = None, head
        while curr and curr != slow:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first, second = prev, slow
        res = first.val + second.val
        while first and second:
            res = max(res, first.val + second.val)
            first, second = first.next, second.next
        return res

