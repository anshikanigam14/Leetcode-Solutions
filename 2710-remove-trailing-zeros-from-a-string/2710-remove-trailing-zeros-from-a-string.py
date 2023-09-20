class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_list = list(num)
        # print(num_list)

        for i in range(len(num_list)-1,-1,-1):
            print(num_list[i])
            if num_list[i] == '0':
                num_list.pop(i)
            else:
                break

        output = ''.join(num_list)
        return output
        