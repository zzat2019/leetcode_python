# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
# 示例：
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line_1 = {"q","w","e","r","t","y","u","i","o","p"}
        line_2 = {"a","s","d","f","g","h","j","k","l"}
        line_3 = {"z","x","c","v","b","n","m"}
        ls = []
        for word in words:
            # issubset 判断集合是否包含在指定集合内返回ture f
            if set(word.lower()).issubset(line_1) or set(word.lower()).issubset(line_2) or set(word.lower()).issubset(line_3):
              ls.append(word)
        return  ls