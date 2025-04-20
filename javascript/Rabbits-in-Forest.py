from collections import Counter
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total=0
        for x,freq in count.items():
            group_size=x+1
            group=math.ceil(freq/group_size)
            total+=group*group_size
        return total