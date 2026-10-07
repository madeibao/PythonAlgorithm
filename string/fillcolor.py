

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        color = image[sr][sc]
        image[sr][sc] = newColor
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = sr + dx, sc + dy
            if x >= 0 and x < len(image) and y >= 0 and y < len(image[0]) and image[x][y] == color:
                self.floodFill(image, x, y, newColor)
        return image


if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    solution = Solution()
    result = solution.floodFill(image, sr, sc, newColor)
    print(result)  # Output: [[2,2,2],[2,2,0],[2,0,1]]