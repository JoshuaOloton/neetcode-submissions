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
        curr = res
        for i in range(len(nodes)):
            node = nodes[i]
            curr.next = ListNode(node)
            curr = curr.next 

        return res.next
