# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        arr1 = []
        arr2 = []
        if list1 is not None:
            arr1.append(list1.val)
            curr = list1.next
            while curr:
                arr1.append(curr.val)
                curr = curr.next

        if list2 is not None:
            arr2.append(list2.val)
            curr = list2.next
            while curr:
                arr2.append(curr.val)
                curr = curr.next
        arr1.extend(arr2)
        arr1.sort()
        ans = ListNode(arr1[0])
        dummy = ans
        for val in arr1[1:]:
            dummy.next = ListNode(val)
            dummy = dummy.next
        return ans

        