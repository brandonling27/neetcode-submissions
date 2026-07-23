class Solution:
    directions = [[0,1], [1, 0], [-1,0], [0,-1]]
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numColumns = len(grid[0])
        seenGrid = [[False for _ in range(numColumns)] for _ in range(numRows)]
        totalIslands = 0
        for i in range(numRows):
            for j in range(numColumns):
                if not seenGrid[i][j] and grid[i][j] == '1':
                    # do dfs
                    totalIslands += 1
                    self.doDfs(grid, seenGrid, i, j)
        return totalIslands

    def checkInBounds(self, x,y, numRows, numCols):
        if x < 0 or x >= numRows:
            return False
        if y < 0 or y >= numCols:
            return False
        return True

    def doDfs(self, grid, seenGrid, x, y):
        if not self.checkInBounds(x,y, len(grid), len(grid[0])):
            return
        # should be in bounds here
        if seenGrid[x][y]:
            return
        # should be not seen here
        seenGrid[x][y] = True
        if grid[x][y] == '0':
            return
        for dx, dy in self.directions:
            self.doDfs(grid, seenGrid, x+dx, y+dy)