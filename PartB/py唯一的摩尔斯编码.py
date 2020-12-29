

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        chara = [chr(i) for i in range(97,123)]
        chara_to_code = {chara[i]:code[i] for i in range(0,26)}
 
        chs = []
        ch = ''
        for word in words:
            for c in word:
                ch = ch + chara_to_code[c]
            chs.append(ch)
            ch = ''
        print(chs)
        return len(set(chs))


if __name__ == '__main__':
    s =Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(s.uniqueMorseRepresentations(str2))