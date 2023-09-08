class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1 = len(str1)
        len_str2 = len(str2)
        min_len_str = min(len_str1, len_str2)
        max_common = ""
        for i in range(0, min_len_str):
            char_1 = str1[i]
            char_2 = str2[i]
            if char_1 == char_2:
                max_common = max_common + char_1
            else:
                break
        print("max common", max_common)
        print("CAND GCD", max_common)
        if len(str1.replace(max_common, "")) == 0 and len(str2.replace(max_common, "")) == 0:
                return max_common 
        
        for i in range(1, len(max_common)):
            cand_gcd = max_common[:-i]
            print("CAND GCD", cand_gcd)
            if len(str1.replace(cand_gcd,"")) == 0 and len(str2.replace(cand_gcd, "")) == 0:
                return cand_gcd              
        return ''