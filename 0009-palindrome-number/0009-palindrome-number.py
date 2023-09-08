class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        if(str(x)==str(y)):
            return True
        