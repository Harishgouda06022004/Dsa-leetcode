class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves=0
        if maxDoubles==0:
            return target-1
        while target>1:
            if target%2==0 and maxDoubles>0:
                target=target//2
                maxDoubles-=1
            else:
                if maxDoubles==0:
                    moves+=(target-1)
                    break
                target-=1
            moves+=1
        return moves


        print(moves)
        
        return moves

                

