class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal_list = []
        curr_pop_char = 'L'
        counter = 0
        for char in s:
            if len(bal_list) == 0:
                bal_list.append(char)
                if char == 'L':
                    curr_pop_char = 'R'
            elif char != curr_pop_char:
                bal_list.append(char)
            else:
                bal_list.pop()
                if len(bal_list) == 0:
                    counter += 1
                    curr_pop_char = 'L'
        return counter
        