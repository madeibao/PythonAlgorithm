

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # 北、东、南、西
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        x, y = 0, 0
        max_dist_sq = 0
        obstacle_set = set(map(tuple, obstacles))
        
        for cmd in commands:
            if cmd == -2:
                # 左转90
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                # 右转90
                dir_idx = (dir_idx + 1) % 4
            else:
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        # 碰到障碍，停止前进
                        break
        return max_dist_sq



if __name__ == '__main__':
    commands = [4, -1, 3]
    obstacles = []
    print(Solution().robotSim(commands, obstacles))

