class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for s in stones:
            for j in jewels:
                if s == j:
                    counter += 1
        return counter
        