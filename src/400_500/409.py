class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        dictで持っとく
        """
        dic = {}
        for st in s:
            if st in dic:
                dic[st] += 1
            else:
                dic[st] = 1

        # valueで降順でsort
        dic2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # print(dic2)
        # print(type(dic2[0]))
        # print(dic2[0][1])
        max_p = 0
        flg = True
        for t in dic2:
            val = t[1]
            if(val % 2 == 0):
                max_p += val
            elif(flg):
                max_p += val
                flg = False
            else:
                max_p += (val - 1)
        return max_p


if __name__ == "__main__":
    sol = Solution()
    s = "abccccdd"
    print(sol.longestPalindrome(s=s))

    s = "a"
    print(sol.longestPalindrome(s=s))
