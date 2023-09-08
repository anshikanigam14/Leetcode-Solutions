class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        alpha_1 = s[0]
        alpha_2 = s[3]
        num_1 = int(s[1])
        num_2 = int(s[4])
        output = []
        if num_1 != num_2:
            for i in range(0, len(alphabets)):
                if alphabets[i] == alpha_1:
                    start = i
            for j in range(start, len(alphabets)):
                for num in range(min(num_1, num_2), max(num_1, num_2)+1):
                    output.append(alphabets[j]+str(num))
                if alphabets[j] == alpha_2:
                    break
        else:
            for i in range(0, len(alphabets)):
                if alphabets[i] == alpha_1:
                    start = i
                    for j in range(start, len(alphabets)):
                        output.append(alphabets[j]+ str(num_1))
                        if alphabets[j] == alpha_2:
                            break
        return output
