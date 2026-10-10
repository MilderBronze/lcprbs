class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nei, wt in adj[node]:
                new_dist = d + wt
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        ans = max(dist[1:])

        return -1 if ans == float('inf') else ans
