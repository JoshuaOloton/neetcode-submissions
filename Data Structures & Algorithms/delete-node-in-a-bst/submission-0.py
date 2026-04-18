# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else: # found node to delete
            # case 1 and 2 - node has 0 or 1 children
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # case 3 - node has 2 children
            # find smallest node in right subtree - preorder successor
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        
        return root