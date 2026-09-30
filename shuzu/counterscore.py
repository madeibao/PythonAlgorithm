

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = counter = 0

        for s in events:
            if s == "W":
                counter += 1
                if counter == 10:
                    break
            elif len(s) > 1:  # "WD" "NB"
                score += 1
            else:  # 数字
                score += int(s)
        return [score, counter]

if __name__=="__main__":
    events = ["1","4","W","6","WD"]
    print(Solution().scoreValidator(events))