class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        s = list(s.strip().split(" "))
        for val in s:
            if len(val) >= 1:
                output.append(val)
        # reverse words of list
        return(" ".join(output[::-1]))
        