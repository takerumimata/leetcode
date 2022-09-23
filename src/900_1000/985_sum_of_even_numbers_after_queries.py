class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sum = 0
        first_flag = True
        for value, index in queries:
            previous_num = nums[index]
            nums[index] += value
            if first_flag:
                for num in nums:
                    if num % 2 == 0:
                        sum += num
                answer.append(sum)
                first_flag = False
            else:
                # nums[index] が偶数の場合
                if nums[index] % 2 == 0:
                    if previous_num % 2 == 0:
                        sum += value
                    else:
                        sum += nums[index]
                # nums[index] が奇数の場合
                else:
                    if previous_num % 2 == 0:
                        sum -= previous_num

                answer.append(sum)
        return answer
