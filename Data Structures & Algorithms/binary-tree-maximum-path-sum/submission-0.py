# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(node):
            if not node:
                return 0

            lsum = dfs(node.left)
            rsum = dfs(node.right)

            straight = max(lsum + node.val, rsum + node.val, node.val)
            branch = max(straight, lsum + rsum + node.val)

            nonlocal res
            res = max(res, branch)
            
            return straight
        
        dfs(root)
        return res