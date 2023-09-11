class Solution:
    def finalString(self, s: str) -> str:
        output_rev = ""

        for w in range(len(s)):
            print("w",w)
            if s[w] == 'i':
                print("w",w)
                output_rev = output_rev[::-1]
                print("output reverse so far:", output_rev)
            else:
                output_rev = output_rev + s[w]
                print("output without i:",output_rev)

        print("final output", output_rev)
        return output_rev