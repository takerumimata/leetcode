class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """文字列をsortして、sortした結果が同じか判定する
        """
        s = sorted(s)
        t = sorted(t)
        if(s == t):
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
