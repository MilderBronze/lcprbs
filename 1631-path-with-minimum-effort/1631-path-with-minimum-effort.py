class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        q = []
        heapq.heappush(q, ([0, 0], 0))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m = len(heights)
        n = len(heights[0])
        dist = [[1e9 for _ in range(n)] for _ in range(m)]
        dist[0][0] = 0
        while q:
            [x, y], diff = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return diff
            if diff > dist[x][y]:
                continue
            for i, j in directions:
                ni = x + i
                nj = y + j
                if 0 <= ni < m and 0 <= nj < n:
                    new_diff = max(abs(heights[ni][nj] - heights[x][y]), diff)
                    if new_diff < dist[ni][nj]:
                        dist[ni][nj] = new_diff
                        heapq.heappush(q,([ni, nj], new_diff))
