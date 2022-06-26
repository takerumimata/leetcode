from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    output = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                output.append(nums[i])
                output.append(nums[j])
                print(output)
                return output
