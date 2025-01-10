class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr=sorted(arr)
        target=sorted(target)
        if target==arr:
            return True
        return False