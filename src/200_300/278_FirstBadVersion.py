# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """二分探索
        """
        left = 1
        right = n
        mid = (left + right) / 2
        while(True):
            if(isBadVersion(mid) and not (isBadVersion(mid + 1))):
                return mid
        return 0
