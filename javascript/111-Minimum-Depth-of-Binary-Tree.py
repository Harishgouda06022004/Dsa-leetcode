# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return float('inf')
            if node.left is None  and node.right is None:
                return 1
            return 1+min(depth(node.left),depth(node.right))
        if root is None:
            return 0
        return depth(root)