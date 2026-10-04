class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, price in flights:
            adj[u].append((v, price))

        dist = [[1e9] * (k + 2) for _ in range(n)] # samajh gaya

        q = []
        heapq.heappush(q, (0, src, 0))
        dist[src][0] = 0

        while q:
            cost, node, stops = heapq.heappop(q)

            if node == dst:
                return cost

            if stops == k + 1:
                continue

            for neighbor, price in adj[node]:
                new_cost = cost + price
                new_stops = stops + 1

                if new_cost < dist[neighbor][new_stops]:
                    dist[neighbor][new_stops] = new_cost
                    heapq.heappush(q, (new_cost, neighbor, new_stops))

        return -1