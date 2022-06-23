import math
import re
from pip import main


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """方針
        スペースなどの特殊文字を削除して文字列を作る
        """
        s_alpha = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        print(s_alpha)

        length_divide_by_two = math.floor(len(s_alpha))

        for i in range(length_divide_by_two):
            if (s_alpha[i] != s_alpha[-1-i]):
                print(s_alpha[i])
                print(s_alpha[-1-i])
                return False
        return True


if __name__ == '__main__':
    input = "A man, a plan, a canal: Panama"
    ret = Solution()
    ans = ret.isPalindrome(s=input)
    print(ans)
