# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                # Base case: an empty node has a height of 0
                return 0
            
            # Recursively find the height of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # The diameter at THIS node is the sum of left and right heights
            # We update the global maximum if this path is longer
            self.res = max(self.res, left + right)

            # Return the height of this node to its parent
            return 1 + max(left, right)

        dfs(root)
        return self.res
    




        