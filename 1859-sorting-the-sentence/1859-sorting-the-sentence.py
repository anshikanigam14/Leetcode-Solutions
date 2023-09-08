import re
class Solution:
    def sortSentence(self, s: str) -> str:
        pattern = r'[0-9]'
        word_dict = {}
        output = ""
        s_split = s.split()
        for word in s_split:
            for i in range(0, len(word)):
                if word[i].isnumeric():
                    word_new = re.sub(pattern,'', word)
                    word_dict.update({int(word[i]):word_new})
        word_dict = dict(sorted(word_dict.items()))
        output = ' '.join(word_dict.values()).strip()
        return output










        