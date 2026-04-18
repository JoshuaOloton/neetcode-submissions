# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        first = head
        second = head.next

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        
        head.next = None
        head = first

        return head
        