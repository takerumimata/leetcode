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
        """方針
        探索二分木の関係性
        left < 親 < right

        親 < 探索したい２つの値 -> 右側をroo
        探索したい２つの値 < 親 -> 左がわを親に
        """
        left_v = p.val
        right_v = q.val
        cur = root
        path_p = []
        # find p
        while(cur):
            if(cur.val < left_v and cur.val < right_v):  # 右側を探索していく
                cur = cur.right
            elif(cur.val > left_v and cur.val > right_v):  # 左側を探索していく
                cur = cur.left
            else:
                return cur
