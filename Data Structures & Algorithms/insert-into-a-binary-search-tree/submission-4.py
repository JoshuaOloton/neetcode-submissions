# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        cur = root
        while cur:
            if val > cur.val:
                if not cur.right:
                    break
                cur = cur.right
            else:
                if not cur.left:
                    break
                cur = cur.left
        
        node = TreeNode(val)
        if val > cur.val:
            cur.right = node
        else:
            cur.left = node

        return root