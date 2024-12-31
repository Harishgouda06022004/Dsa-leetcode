# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def ismirror(left,right):
            if right is None and left is None:
                return True
            if right is None or left is  None:
                return False
            if left.val!=right.val:
                return False
            return ismirror(left.left, right.right) and ismirror(left.right, right.left)
        return ismirror(root.left,root.right)