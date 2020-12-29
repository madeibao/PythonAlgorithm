给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。

数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "d"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "g"
输出: "j"

输入:
letters = ["c", "f", "j"]
target = "j"
输出: "c"


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lett2 = sorted(letters)
        temp = ""
        if ord(target) >= ord(lett2[-1]):
            return lett2[0]
        else:
            for i in range(len(letters)):
                if ord(target) < ord(letters[i]):
                    temp = letters[i]
                    break

        return temp


if __name__ == '__main__':
    s = Solution()
    letters = ["c", "f", "j"]
    target = "j"
    print(s.nextGreatestLetter(letters, target))




