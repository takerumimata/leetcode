# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """二分探索
        """
        if(isBadVersion(1)):
            return 1
        left = 1  # not bad
        right = n  # bad
        mid = int((left + right) / 2)
        while(True):
            if(not(isBadVersion(mid)) and isBadVersion(mid + 1)):
                return int(mid + 1)
            elif(isBadVersion(mid)):
                # midがbad
                right = mid
                mid = int((left + right) / 2)  # 基本的に繰り下げ
            else:
                # midがnot bad
                left = mid
                mid = int((left + right) / 2)
        return 0
