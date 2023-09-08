class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        output = ""
        vowels_list = []
        for char in s:
            if char in vowels:
                vowels_list.append(char)
  
        for char in s:
            if char in vowels:
                output += vowels_list.pop()
            else:
                output += char
        return output
        