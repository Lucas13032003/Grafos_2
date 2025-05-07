import heapq

class Solution(object):
    def findAnswer(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[bool]
        """

        # Criar o grafo como lista de adjacência
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(source):
            dist = [float('inf')] * n
            dist[source] = 0
            heap = [(0, source)]

            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(heap, (dist[v], v))

            return dist

        # Calcular distâncias mínimas a partir de 0 e de n-1
        dist_from_start = dijkstra(0)
        dist_from_end = dijkstra(n - 1)
        min_total = dist_from_start[n - 1]

        # Verificar se a aresta faz parte de algum caminho mínimo
        result = []
        for u, v, w in edges:
            ok = (
                dist_from_start[u] + w + dist_from_end[v] == min_total or
                dist_from_start[v] + w + dist_from_end[u] == min_total
            )
            result.append(ok)

        return result
