class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        print(s_list)
        output = ""

        for word in s_list:
            # print(word)
            for w in range(len(word)-1,-1, -1):
                output = output + word[w]
                # print(output)
            output = output + " "

        return output.strip() 
        