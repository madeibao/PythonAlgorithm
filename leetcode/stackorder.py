from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        判断 popped 是否是 pushed 对应栈的弹出序列（LeetCode 946 / 剑指 Offer 31）

        思路：模拟压栈过程。
        依次将 pushed 中的元素压入辅助栈，每压入一个元素，
        就检查栈顶是否等于 popped 中当前待弹出的元素，
        若相等则循环弹出。最后栈为空说明 popped 是合法的弹出序列。

        时间复杂度 O(n)，空间复杂度 O(n)
        """
        stack = []          # 辅助栈，模拟压入/弹出过程
        j = 0               # popped 的遍历指针
        for x in pushed:
            stack.append(x)                 # 压入当前元素
            # 栈顶与待弹出元素相同，就一直弹出
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return stack is None    # 全部能弹出则合法


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        # (pushed, popped, 期望结果, 说明)
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True,  "合法：4,5,3,2,1 可以按此顺序弹出"),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False, "非法：1 不可能在 2 之前弹出"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True,  "合法：压一个弹一个"),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], True,  "合法：全部压入后依次弹出"),
        ([1],             [1],             True,  "单元素，合法"),
        ([1],             [2],             False, "单元素，不匹配"),
        ([],              [],              True,  "空序列，合法"),
    ]

    for pushed, popped, expected, desc in test_cases:
        result = sol.validateStackSequences(pushed, popped)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] pushed={pushed}, popped={popped} -> {result}  ({desc})")
