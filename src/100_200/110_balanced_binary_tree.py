from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """深さ優先探索で考える
        ①rootがNoneになるまでひたすら探索していって
        ②サブツリーの左右の高さを取得する
        """

        def isHightBalanced(root, isBalance):
            # ツリーがからであるか、バランスが取れていない
            if root is None or not isBalance:
                return 0, isBalance

            # 再帰的に探索を行う
            # 深さ優先探索
            left_height, isBalance = isHightBalanced(
                root=root.left, isBalance=isBalance)
            right_height, isBalance = isHightBalanced(
                root=root.right, isBalance=isBalance)

            # 左右の木の高さを比べる
            if abs(left_height - right_height) > 1:
                isBalance = False

            # 高さは+1して返す
            return max(left_height, right_height) + 1, isBalance

        _, isBalance = isHightBalanced(root, True)
        return isBalance


if __name__ == "__main__":
    pass
