
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

输入：text = "loonbalxballpoon"
输出：2

输入：text = "leetcode"
输出：0


class Solution:
    def maxNumberOfBalloons(self, text) -> int:
        num1 = text.count('b')
        num2 = text.count('a')
        num3 = text.count('l')
        num4 = text.count('o')
        num5 = text.count('n')

        numN = min(min(num1, num2), num5)
        numM = min(num3, num4)
        num8 = numM //2
        numsum = min(numN, num8)

        return numsum


text = "loonbalxballpoon"
# text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
cc = Solution()
print(cc.maxNumberOfBalloons(text))


