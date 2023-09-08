class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = {}
        output = ""
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        i = 0
        for mychar in key:
            if mychar == " ":
                continue
            if not key_dict.get(mychar):
                key_dict.update({mychar: alphabets[i]})
                # print(key_dict)
                # print(i)
                i += 1

        for m in message:
            if m != " ":
                output += key_dict.get(m) 
            else:
                output += " "
                # print(output)

        # print(message)
        # print(key_dict)
        # print(output)
        return output