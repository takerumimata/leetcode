from re import A
from typing import List
import sys


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """再帰を利用することで解く
        """
        def fill(image, sr, sc, prev, color):
            print(sr)
            print(sc)
            if (sr >= 1):
                if(image[sr - 1][sc] == prev and image[sr - 1][sc] != color):
                    image[sr - 1][sc] = color
                    return fill(image, sr - 1, sc, prev, color)
            if (sr < m - 1):
                if(image[sr + 1][sc] == prev and image[sr + 1][sc] != color):
                    image[sr + 1][sc] = color
                    return fill(image, sr + 1, sc, prev, color)
            if (sc >= 1):
                if(image[sr][sc - 1] == prev and image[sr][sc - 1] != color):
                    image[sr][sc - 1] = color
                    return fill(image, sr, sc - 1, prev, color)
            if (sc < n - 1):
                if(image[sr][sc + 1] == prev and image[sr][sc + 1] != color):
                    image[sr][sc + 1] = color
                    return fill(image, sr, sc + 1, prev, color)

        # 隣が自身の前の色と同じ色ならそこを起点にしてまた塗り替えていく
        m = len(image)
        n = len(image[0])
        prev = image[sr][sc]
        image[sr][sc] = color
        fill(image=image, sr=sr, sc=sc, prev=prev, color=color)

        return image


class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        ①再帰を利用することで解く
        -> アルゴリズム自体は問題ないが、recursionのしすぎで怒られる
        ②再帰をloopで書く
        """
        sys.setrecursionlimit(1000000)
        # 隣が自身の前の色と同じ色ならそこを起点にしてまた塗り替えていく
        m = len(image)
        n = len(image[0])
        prev = image[sr][sc]
        image[sr][sc] = color
        cur_sr = sr
        cur_sc = sc

        if (sr >= 1):
            if(image[sr - 1][sc] == prev and image[sr - 1][sc] != color):
                self.floodFill(image, sr - 1, sc, color)
        if (sr < m - 1):
            if(image[sr + 1][sc] == prev and image[sr + 1][sc] != color):
                self.floodFill(image, sr + 1, sc, color)
        if (sc >= 1):
            if(image[sr][sc - 1] == prev and image[sr][sc - 1] != color):
                self.floodFill(image, sr, sc - 1, color)
        if (sc < n - 1):
            if(image[sr][sc + 1] == prev and image[sr][sc + 1] != color):
                self.floodFill(image, sr, sc + 1, color)
        return image


if __name__ == "__main__":
    sol = Solution()
    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr1 = 1
    sc1 = 1
    color1 = 2
    ret = sol.floodFill(image=image1, sr=sr1, sc=sc1, color=color1)
    print(ret)

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    ret = sol.floodFill(image=image, sr=sr, sc=sc, color=color)
    print(ret)
