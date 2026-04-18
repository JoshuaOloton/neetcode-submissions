# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head

        while temp:
            temp = temp.next
            l += 1
        
        if l - n == 0:
            head = head.next
            return head

        i = 1
        curr = head
        while curr.next:
            if i == l - n:
                curr.next = curr.next.next
            else:
                curr = curr.next
            i += 1
        
        return head

            
