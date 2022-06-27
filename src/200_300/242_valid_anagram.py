class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """まずは文字の長さが一致していること
        """
        len_s = len(s)
        len_t = len(t)
        if(len_s != len_t):
            print("length is not same")
            return False
        else:
            for i in range(len_s):
                rem_s = s[i]  # 取り除く文字
                rem_t = t.find(rem_s)  # 文字があるか、あれば位置を返す
                if(rem_t == -1):
                    return False
                else:
                    t = list(t)
                    t[rem_t] = ""
                    t = "".join(t)
            return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
