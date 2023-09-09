class Solution:
    def toLowerCase(self, s: str) -> str:
        output = ""
        for i in s:
            output = output + i.lower() 
        return output
        