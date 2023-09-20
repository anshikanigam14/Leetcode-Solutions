class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        output = ""
        for w in words:
            if w[::-1] == w:
                output = w[::-1]
                break
            else:
                output = ""
        return output
        