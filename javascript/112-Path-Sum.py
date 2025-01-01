# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def Path(node,currentSum):
            if node is None:
                return False
            if not node.left and not node.right:
                return currentSum==node.val
            return Path(node.left,currentSum-node.val) or Path(node.right,currentSum-node.val)
        return Path(root,targetSum)