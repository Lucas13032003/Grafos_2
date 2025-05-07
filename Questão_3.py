from typing import List

# Estrutura de dados Union-Find (Disjoint Set Union) com Compressão de Caminho e União por Rank
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Pai de cada nó
        self.rank = [0] * n  # Rank de cada nó para a união por rank

    def find(self, x):
        # Encontra o representante do conjunto de x com compressão de caminho
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compressão de caminho
        return self.parent[x]

    def union(self, x, y):
        # Une os conjuntos de x e y
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # União por rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # Passo 1: Ordenar as arestas por peso
    edges.sort(key=lambda edge: edge[2])  # Ordenar as arestas com base no peso (edge[2])
    
    # Passo 2: Inicializar a estrutura Union-Find
    uf = UnionFind(n)
    
    mst_weight = 0  # Para armazenar o peso total da MST
    mst_edges = 0  # Para contar o número de arestas na MST
    
    # Passo 3: Processar as arestas
    for u, v, w in edges:
        u -= 1  # Converter para índice baseado em zero
        v -= 1  # Converter para índice baseado em zero
        
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w  # Adiciona o peso da aresta à MST
            mst_edges += 1  # Incrementa o número de arestas na MST
            
            # Se já temos n-1 arestas, a MST está completa
            if mst_edges == n - 1:
                break
    
    return mst_weight  # Retorna o peso total da MST
