from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """二分探索すれば良い
        """
        list_length = len(nums)
        mid = int(list_length / 2)
        left = 0
        right = list_length

        if(nums[0] == target):
            return 0

        while(right - left != 1):
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                right = mid
                mid = int((right + left) / 2)
            else:
                left = mid
                mid = int((right + left) / 2)
        return -1


if __name__ == "__main__":
    sol = Solution()
    test_case = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(sol.search(test_case, target))
    test_case = [-1, 0, 3, 5, 9, 12, 15]
    target = 1
    print(sol.search(test_case, target))
