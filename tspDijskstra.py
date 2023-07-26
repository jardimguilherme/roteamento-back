import heapq

def dijkstra(grafo, inicio, fim):
    dist = {node: float('infinity') for node in grafo}
    dist[inicio] = 0
    pq = [(0, inicio)]
    
    while pq:
        (distancia, vertice_atual) = heapq.heappop(pq)
        
        if vertice_atual == fim:
            return distancia

        if distancia == dist[vertice_atual]:
            for vizinho, infos in grafo[vertice_atual].items():
                custo = infos['weight']
                distancia_antiga = dist[vizinho]
                distancia_nova = distancia + custo
                if distancia_nova < distancia_antiga:
                    dist[vizinho] = distancia_nova
                    heapq.heappush(pq, (distancia_nova, vizinho))
    return float('infinity')

def caixeiro_viajante(grafo, vertices_interesse, inicio):
    caminho = [inicio]
    vertices_interesse = set(vertices_interesse)
    
    while vertices_interesse:
        proximo_vertice = min(vertices_interesse, key=lambda vertice: dijkstra(grafo, inicio, vertice))
        vertices_interesse.remove(proximo_vertice)
        caminho.append(proximo_vertice)
        inicio = proximo_vertice
    return caminho