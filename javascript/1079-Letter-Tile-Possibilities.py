from itertools import permutations
class Solution(object):
    def numTilePossibilities(self, tiles):
        if len(tiles)==1:
            return 1
        all_permutations=set()
        for i in range(1,len(tiles)+1):
            all_permutations.update(permutations(tiles,i))
        return len(all_permutations)