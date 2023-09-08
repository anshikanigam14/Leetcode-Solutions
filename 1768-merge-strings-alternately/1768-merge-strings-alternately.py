class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        min_len_word = min(len_word1, len_word2)
        output = ""

        for i in range(0, min_len_word):
            output = output + word1[i]
            output = output + word2[i]

        if len_word1 > len_word2:
            output = output + word1[min_len_word:]
        else:
            output = output + word2[min_len_word:] 
        return output 
        