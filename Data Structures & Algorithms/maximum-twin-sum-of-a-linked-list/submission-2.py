# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        first, second = prev, slow
        res = first.val + second.val
        while first:
            res = max(res, first.val + second.val)
            first, second = first.next, second.next
        return res

