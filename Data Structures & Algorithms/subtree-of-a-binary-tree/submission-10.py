# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        
        if tree1 and tree2 and tree1.val == tree2.val:
            return (
                self.sameTree(tree1.left, tree2.left) and
                self.sameTree(tree1.right, tree2.right)
            )
            
        return False
        