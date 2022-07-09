"""235. Lowest Common Ancestor of a Binary Search Tree

url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

問題の定義について
LCA（Lowest common ancestor）ってそもそも何？

二つのノードpとqが与えられた時に、共通の祖先となる最も近いノードを指すらしい。この時、pはpの祖先として取り扱うことができる。
そのため、pとqが直接繋がっている場合、p自身がLCAにあたる
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass
