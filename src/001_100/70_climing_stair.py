class Solution:
    def climbStairs(self, n: int) -> int:
        """memo化再帰
        n段までの到達路の合計

        44段 - > 45段...１通り
        Count(n-2) + Count(n-1)
        """

        memo = [-1]*(n+1)

        def count_n(i: int) -> int:
            if(i == 1):
                return 1
            elif(i == 2):
                return 2
            elif(memo[i] != -1):
                return memo[i]
            else:
                memo[i] = count_n(i-2) + count_n(i-1)
                return memo[i]

        return count_n(n)


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.climbStairs(n))
