class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def visited(row, col, grid):

            max_row = len(grid)
            max_col = len(grid[0])

            if (row-1) >= 0 and grid[row-1][col] == "1":
                grid[row-1][col] = "0"
                visited(row-1, col, grid)
            if (col-1) >= 0 and grid[row][col-1] == "1":
                grid[row][col-1] = "0"
                visited(row, col-1, grid)
            if (row+1) < max_row and grid[row+1][col] == "1":
                grid[row+1][col] = "0"
                visited(row+1, col, grid)
            if (col+1) < max_col and grid[row][col+1] == "1":
                grid[row][col+1] = "0"
                visited(row, col+1, grid)

            return "0"

        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    visited(row, col, grid)
                    island += 1
        return island


