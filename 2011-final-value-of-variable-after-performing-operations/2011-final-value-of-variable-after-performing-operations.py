class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for val in operations:
            if val in ["--X", "X--"]:
                X = X - 1
            else:
                X = X + 1
        return X