class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # moves=0
        # if maxDoubles==0:
        #     return target-1
        # while target>1:
        #     if target%2==0 and maxDoubles>0:
        #         target//2
        #         moves+=1
        #     else:
        #         moves+=target-1

        # print(moves)
        moves = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    # Only subtraction is left
                    moves += (target - 1)
                    break
                target -= 1
            moves += 1
        return moves

                

