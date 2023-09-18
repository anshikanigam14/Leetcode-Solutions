class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = 0

        if len(s)%2 != 0:
            mid_len = int(round(len(s)/2))
            for i in range(len(s)-1,mid_len-1,-1):
                # print(s[i], s[j])
                # print(i,j)
                s[i], s[j] = s[j], s[i]  
                j = j+1
                # print(s)
                # print("")
        else:
            mid_len = int(len(s)/2)
            for i in range(len(s)-1,mid_len-1,-1):
                # print(s[i], s[j])
                # print(i,j)
                s[i], s[j] = s[j], s[i]  
                j = j+1
                # print(s)
                # print("")
    