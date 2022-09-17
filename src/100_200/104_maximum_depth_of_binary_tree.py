# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        return self.bfs(root, 0)

    def bfs(self, root: Optional[TreeNode], depth: int) -> int:
        # left or rightにnodeがなければ
        if(root == None):
            return depth
        if(root.left == None and root.right == None):
            return depth
        return max(self.bfs(root.left, depth + 1), self.bfs(root.right, depth + 1))
