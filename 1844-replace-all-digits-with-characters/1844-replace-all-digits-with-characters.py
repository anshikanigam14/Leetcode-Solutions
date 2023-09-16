class Solution:
    def replaceDigits(self, s: str) -> str:
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        output = ""

        for i in range(0,len(s)):
            if s[i].isnumeric():
                end = int(s[i])
                print(end)
                for j in range(0,len(letters)):
                    if letters[j] == s[i-1]:
                        output = output + letters[j+end]
                    else:
                        continue
            else:
                output = output + s[i]
        return output