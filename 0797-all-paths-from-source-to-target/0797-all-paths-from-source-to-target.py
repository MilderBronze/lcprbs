class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        length_of_graph = len(graph)
        src = 0
        dest = length_of_graph - 1
        ans = []
        visited = [False for _ in range(length_of_graph)]
        path_visited = [src]
        visited[src] = True
        self.dfs(graph, src, dest, 0, ans, path_visited, visited)
        return ans

    def dfs(self, adj, src, dest, node, ans, path_visited, visited):
        if node == dest:
            ans.append(path_visited.copy()) # take a snapshot of an accurate path, store it, then keep modifying the path.
            return
        for neighbor in adj[node]:
            if visited[neighbor] is False:
                path_visited.append(neighbor)
                visited[neighbor] = True
                self.dfs(adj, src, dest, neighbor, ans, path_visited, visited)
                visited[neighbor] = False
                path_visited.pop()
        