class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        counter = 0
        counter_list = []
        for val in sentences:
            print(val)
            for char in val:
                print(char)
                if char == ' ':
                    counter += 1
            counter_list.append(counter)
            counter = 0
        print(counter_list)
        return max(counter_list)+1 

        