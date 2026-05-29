class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def countIslands(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            visit.add((r, c))

            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in neighbors:
                if (r + dr, c + dc) not in visit:
                    countIslands(r + dr, c + dc)

        for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == "1" and (r, c) not in visit:
                        countIslands(r, c)
                        count += 1


        return count



                    
