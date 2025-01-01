# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def Path(node,currentSum,path):
            if node is None:
               return 
            path.append(node.val)
            if not node.left and not node.right and currentSum == node.val:
                result.append(list(path))
            Path(node.left, currentSum - node.val, path)
            Path(node.right, currentSum - node.val, path)
            path.pop()
        Path(root,targetSum,[])
        return result
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         result = []

#         def Path(node, currentSum, path):
#             # Base case: If node is None, return immediately
#             if node is None:
#                 return

#             # Add the current node value to the path
#             path.append(node.val)

#             # Check if it's a leaf node and the currentSum matches the target
#             if not node.left and not node.right and currentSum == node.val:
#                 result.append(list(path))  # Add a copy of the current path to the result

#             # Recur for left and right subtrees with updated currentSum
#             Path(node.left, currentSum - node.val, path)
#             Path(node.right, currentSum - node.val, path)

#             # Backtrack to explore other paths
#             path.pop()

#         # Start the recursion with the root node and the targetSum
#         Path(root, targetSum, [])
#         return result
