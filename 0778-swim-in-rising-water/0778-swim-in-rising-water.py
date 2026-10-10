class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        q = []
        heapq.heappush(q, [grid[0][0], 0, 0]) # distance, u, v
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        row_length = len(grid)
        col_length = len(grid[0])
        visited = [[False for i in range(col_length)] for _ in range(row_length)]
        visited[0][0] = True
        while q:
            [distance, u, v] = heapq.heappop(q)
            if u == row_length - 1 and v == col_length - 1:
                return distance

            for row, col in directions:
                ni = row + u
                nj = col + v
                if 0 <= ni < row_length and 0 <= nj < col_length and visited[ni][nj] == False:
                    new_distance = max(distance, grid[ni][nj])
                    heapq.heappush(q, [new_distance, ni, nj])
                    visited[ni][nj] = True