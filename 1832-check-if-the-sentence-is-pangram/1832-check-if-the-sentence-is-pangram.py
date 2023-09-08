class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        num = 0
        for i in alphabets:
            if i in sentence:
                num += 1
        if num >= 26:
            return True
        else:
            return False
        