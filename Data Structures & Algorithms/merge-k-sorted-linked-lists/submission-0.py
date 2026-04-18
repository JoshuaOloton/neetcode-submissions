# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            temp = l
            while temp:
                nodes.append(temp.val)
                temp = temp.next
        nodes.sort()

        if len(nodes) == 0:
            return None

        res = ListNode()
        head = res
        for i in range(len(nodes)-1):
            node = nodes[i]
            res.val = node
            res.next = ListNode()
            res = res.next
 
        res.val = nodes[-1]

        return head
