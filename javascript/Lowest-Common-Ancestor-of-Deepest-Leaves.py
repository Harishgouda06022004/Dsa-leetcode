# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,depth):
            if not node:
                return(None,depth+1)

            left_node,left_depth=dfs(node.left,depth+1)
            right_node,right_depth=dfs(node.right,depth+1)
            if left_depth>right_depth:
                return left_node,left_depth
            elif right_depth>left_depth:
                return right_node,right_depth
            else:
                return node,left_depth
        node,_=dfs(root,0)
        return node