


from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        for i in range(N):
            if n == 0:
                break

            if flowerbed[i] == 0:
                if i == 0:
                    if N == 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                elif i == N - 1:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n == 0


if __name__ == "__main__":
	s= Solution()
	flowerbed = [1,0,0,0,1]
	n = 1











