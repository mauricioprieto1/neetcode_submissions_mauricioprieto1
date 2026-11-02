class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numOfIslands = 0
        def dfs(x, y):
            if x < 0 or x > m or y < 0 or y > n:
                return
            
            return
        for i in grid:
            for j in grid[i]:
                if grid[i][j] == '1':
                    dfs(i,j)
        return numOfIslands