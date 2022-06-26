from time import sleep
from typing import Optional


class TreeNode:
    """Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """invert binary tree
        2^(n-1)個のペアを反対から挿入していけばいい

        Args:
            root (Optional[TreeNode]): e.g.) [4,2,7,1,3,6,9]

        Returns:
            Optional[TreeNode]: e.g.) [4,7,2,9,6,3,1]
        """
        num_of_node = len(root)
        # 木の深さを求める
        depth = 0
        tmp = num_of_node
        while(True):
            if(tmp > 0):
                tmp = tmp - 2**depth
                depth += 1
            else:
                break
        print(depth)
        ret = []
        inverted_range_prev = 0
        for i in range(depth):
            # 深さ^i-1 個ノードがあるので、そこの範囲を反転させていけばいい
            invert_length = 2 ** i
            inverted_range_cur = inverted_range_prev + invert_length
            inverted_range = root[inverted_range_prev:inverted_range_cur]
            inverted_range_prev = inverted_range_cur
            print(inverted_range)
            inverted_range.reverse()  # reverseの返り値はNone
            print(inverted_range)
            ret += inverted_range
        return ret


if __name__ == '__main__':
    input = [4, 2, 7, 1, 3, 6, 9]
    inv = Solution()
    sol = inv.invertTree(input)
    print(sol)
