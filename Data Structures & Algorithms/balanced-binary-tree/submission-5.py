# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            return 1 + max(dfs(node.left), dfs(node.right))
        
        if not root:
            return True

        lheight = dfs(root.left)
        rheight = dfs(root.right)

        if abs(rheight - lheight) > 1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)