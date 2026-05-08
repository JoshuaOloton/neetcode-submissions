# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        prev = None
        l, r = head, head.next
        while l:
            l.next = prev
            prev = l
            l = r
            if r:
                r = r.next
        
        return prev