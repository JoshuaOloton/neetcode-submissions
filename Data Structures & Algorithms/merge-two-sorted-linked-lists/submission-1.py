# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev, head, first, second = None, None, list1, list2

        while first and second:
            if first.val < second.val:
                newNode = ListNode(first.val)
                first = first.next
            else:
                newNode = ListNode(second.val)
                second = second.next               
                
            if prev:
                prev.next = newNode
            else:
                head = newNode
            prev = newNode

        while first:
            newNode = ListNode(first.val)

            if prev:
                prev.next = newNode
            else:
                head = newNode
            prev = newNode
            first = first.next

        while second:
            newNode = ListNode(second.val)
            
            if prev:
                prev.next = newNode
            else:
                head = newNode
            prev = newNode
            second = second.next

        return head
