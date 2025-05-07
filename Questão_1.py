import heapq
from collections import defaultdict

class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        def dijkstra(start, graph):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                curr_dist, u = heapq.heappop(heap)
                if curr_dist > dist[u]:
                    continue
                for v, weight in graph[u]:
                    if dist[v] > curr_dist + weight:
                        dist[v] = curr_dist + weight
                        heapq.heappush(heap, (dist[v], v))
            return dist

        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        dist3 = dijkstra(dest, rev_graph)

        min_total = float('inf')
        for i in range(n):
            if dist1[i] < float('inf') and dist2[i] < float('inf') and dist3[i] < float('inf'):
                min_total = min(min_total, dist1[i] + dist2[i] + dist3[i])

        return -1 if min_total == float('inf') else min_total
