class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = list("-"*len(s))
        for i in range(0,len(s)):
            # print( output[i], s[i])
            # output[i] = s[indices[i]]
            output[indices[i]] = s[i]

        return ''.join(output)
