class Solution:
    def allPathsSourceTarget(self, adj: list[list[int]]):
        length_of_graph = len(adj)
        src = 0
        dest = length_of_graph - 1
        queue = deque()
        queue.append([src])
        ans = []
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == dest:
                ans.append(path)
                continue
            for neighbor in adj[node]:
                if neighbor not in path:
                    queue.append(path + [neighbor])
        return ans
        