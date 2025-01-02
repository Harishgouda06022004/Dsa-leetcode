class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        for i in range(rowIndex):
            result = [1] + [result[j] + result[j + 1] for j in range(len(result) - 1)] + [1]
        return result
