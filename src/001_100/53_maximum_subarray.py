from typing import List

from requests import head
"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Dynamic Programmingの予感
        """
        # n = 1の時の最大値
        max = nums[0]
        head = 0

        for i in range(0, len(nums)):
            if(nums[i] < 0):
                continue
            else:
                if(sum(nums[head:i+1]) > max and sum(nums[head:i+1]) > nums[i]):
                    # print(nums[head:i+1])
                    max = sum(nums[head:i+1])
                elif(nums[i] > max and nums[i] > sum(nums[head:i+1])):
                    head = i
                    max = nums[i]
                elif(max > nums[i] and max > sum(nums[head:i+1])):
                    pass
        return max


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(nums=nums))

    nums = [5, 4, -1, 7, 8]
    sol = Solution()
    print(sol.maxSubArray(nums=nums))
