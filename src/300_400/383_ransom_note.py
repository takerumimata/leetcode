class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        magazineに入ってる
        """
        for i in range(len(ransomNote)):
            ch = ransomNote[i]
            index = magazine.find(ch)
            if(index != -1):
                magazine = magazine[:index] + magazine[index + 1:]
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    ransomNote = "a"
    magazine = "b"
    print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))

    ransomNote = "ab"
    magazine = "aa"
    print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))

    ransomNote = "aa"
    magazine = "aab"
    print(sol.canConstruct(ransomNote=ransomNote, magazine=magazine))
