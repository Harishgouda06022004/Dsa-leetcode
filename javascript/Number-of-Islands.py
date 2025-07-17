class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        def markisland(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1':
                return
            grid[r][c]='v'
            markisland(r+1,c)
            markisland(r-1,c)  
            markisland(r,c+1)
            markisland(r,c-1)
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    markisland(r,c)
                    count+=1
        return count