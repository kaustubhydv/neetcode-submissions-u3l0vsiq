# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        L, R = 0, len(arr)-1
        maxSum = arr[L]+arr[R]
        while L < R:
            maxSum = max(maxSum, (arr[L]+arr[R]))
            L += 1
            R -= 1
        return maxSum
