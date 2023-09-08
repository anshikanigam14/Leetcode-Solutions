class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr = "" 
        for w in words:
            for i in range(0,1):
                acr = acr + w[0]
        if acr == s:
            return True
        else:
            return False
