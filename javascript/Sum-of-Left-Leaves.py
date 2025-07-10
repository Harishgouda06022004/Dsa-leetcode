# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        summ=0
        if root.left:
            if not root.left.left and not root.left.right:
                summ+=root.left.val
            else:
                summ+=self.sumOfLeftLeaves(root.left)
        summ+=self.sumOfLeftLeaves(root.right)
        return summ