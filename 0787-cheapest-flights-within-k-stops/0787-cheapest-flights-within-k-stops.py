class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        dist = [1e9] * n
        dist[src] = 0
        
        queue = collections.deque([(0, src, 0)]) # (stops, node, cost)
        while queue:
            stops, u, cost = queue.popleft()
            if stops > k: continue
            
            for v, w in adj[u]:
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    queue.append((stops + 1, v, dist[v]))
                    
        return dist[dst] if dist[dst] != 1e9 else -1