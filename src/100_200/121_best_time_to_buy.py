from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """方針
        下がり続けている間は見なくていい
        """
        max_prof = 0
        start = 0
        end = 1
        while(end < len(prices)):
            if(prices[start] >= prices[end]):
                start = end
                end += 1
            else:
                max_prof = max(max_prof, prices[end] - prices[start])
                end += 1
        return max_prof
