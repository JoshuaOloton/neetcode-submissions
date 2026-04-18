# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        prev_slow = None
        slow = fast = head

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        # prev of slow -> prev_slow is tail of first list
        # slow is head of second list
        prev_slow.next = None
        prev, curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is new head of reversed list
        # merge both lists with heads of head and prev -> l1 and l2
        l1, l2 = head, prev

        while l1:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2

            if not l1_next:
                break

            l2.next = l1_next
            l1, l2 = l1_next, l2_next
