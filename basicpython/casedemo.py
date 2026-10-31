

# class Point:
#     __match_args__ = ("x", "y")  # 声明位置匹配顺序
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def describe(p):
    match p:
        case Point(0, 0):
            return "原点"
        case Point(x, 0):
            return f"在X轴上，x={x}"
        case Point(0, y):
            return f"在Y轴上，y={y}"
        case Point(x, y):
            return f"坐标 ({x}, {y})"
        case _:
            return "不是Point"


if __name__ == "__main__":
    print(describe(Point(0, 0)))
    print(describe(Point(1, 0)))
    print(describe(Point(0, 1)))
    print(describe(Point(1, 1)))
    print(describe("不是"))