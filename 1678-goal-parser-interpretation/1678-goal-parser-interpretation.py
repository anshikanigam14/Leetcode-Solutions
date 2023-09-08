class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        for i in range(0, len(command)):
            if command[i] == 'G':
                output = output+'G'
            elif command[i] == '(' and command[i+1] == ')':
                output = output+'o'
            elif command[i] == '(' and command[i+1] == 'a':
                output = output + 'al'
        return output

        