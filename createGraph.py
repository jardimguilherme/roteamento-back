import math
import networkx as nx

def calcular_distancia_manhattan(ponto1, ponto2):
    lat1, lon1 = ponto1['latitude'], ponto1['longitude']
    lat2, lon2 = ponto2['latitude'], ponto2['longitude']
    
    # converte a latitute de graus para radianos
    lat1_rad, lat2_rad = math.radians(lat1), math.radians(lat2)
    
    # calcula a média da latitude
    mean_lat_rad = (lat1_rad + lat2_rad) / 2

    # calcula lat e long em metros
    dlat = abs(lat1 - lat2) * 111.2 * 1000
    dlon = abs(lon1 - lon2) * 111.2 * math.cos(mean_lat_rad) * 1000

    distancia = dlat + dlon

    return distancia

def criar_grafo(pontos):
    grafo = nx.DiGraph()

    # Mapeia o nome do ponto para o ponto correspondente
    ponto_por_nome = {ponto['nome']: ponto for ponto in pontos}

    lista_adjacencias = {
        'A06/A08' : ['A02/A04', 'Desembarque Internacional', 'Embarque Internacional'],
        'A02/A04' : ['A06/A08', 'E08', 'Desembarque Internacional'],
        'E08' : ['B21', 'Elevador', 'Desembarque Internacional', 'A02/A04'],
        'Desembarque Internacional' : ['A02/A04', 'E08', 'Embarque Internacional', 'A06/A08'],
        'Embarque Internacional' : ['Desembarque Internacional', 'A06/A08', 'Consolidation'],
        'Consolidation' : ['Triagem Internacional', 'Embarque Internacional'],
        'Triagem Internacional' : ['Triagem Local', 'Consolidation'],
        'Triagem Local' : ['Desembarque Doméstico', 'Refeitorio C', 'C02', 'Estacionamento', 'Triagem Internacional', 'Elevador'],
        'Elevador' : ['B02', 'Estacionamento', 'Triagem Local', 'E08', 'B21'],
        'B02' : ['B04', 'Refeitorio C', 'Estacionamento', 'Triagem Local', 'Elevador', 'B21'],
        'B04' : ['B06', 'B02', 'B22', 'B24'],
        'B06' : ['B08', 'B04', 'B28', 'B30', 'B32'],
        'B08' : ['B10', 'B06', 'B30', 'B32', 'HCC', 'Almox', 'Refeitorio B'],
        'B10' : ['B12', 'B08', 'HCC', 'Almox', 'Refeitorio B'],
        'B12' : ['B14', 'B10'],
        'B14' : ['B11/B13', 'B12'],
        'B11/B13' : ['B14', 'Sala Rampa'],
        'Sala Rampa' : ['B11/B13', 'B07/B09'],
        'B07/B09' : ['Sala Rampa', 'HCC', 'B31'],
        'B31' : ['B07/B09', 'B29'],
        'B29' : ['B31', 'B27'],
        'B27' : ['B29', 'B25'],
        'B25' : ['B27', 'B23'],
        'B23' : ['B25', 'B21'],
        'B21' : ['B02', 'Elevador', 'E08'],
        'B22' : ['B24', 'B04', 'B02'],
        'B24' : ['B26', 'B04', 'B22'],
        'B26' : ['B28', 'B06', 'B04', 'B24'],
        'B28' : ['B30', 'B06', 'B26'],
        'B30' : ['B32', 'B08', 'B06', 'B28'],
        'B32' : ['HCC', 'Almox', 'Refeitorio B', 'B08', 'B06', 'B30'],
        'Almox' : ['B10', 'B08', 'B32', 'HCC', 'Refeitorio B'],
        'Refeitorio B' : ['B10', 'B08', 'B32', 'HCC', 'Almox'],
        'HCC' : ['B10', 'B08', 'B32', 'Almox', 'Refeitorio B'],
        'Refeitorio C' : ['C04', 'C02', 'Estacionamento', 'Triagem Local', 'Elevador', 'B02', 'Desembarque Doméstico'],
        'C02' : ['C04', 'N107', 'M08', 'Estacionamento', 'Refeitorio C'],
        'C04' : ['C06', 'Sala da Manutenção', 'C02', 'Refeitorio C'],
        'Sala da Manutenção' : ['C04', 'C06'],
        'C06' : ['C08', 'C04', 'Sala da Manutenção'],
        'C08' : ['C10', 'C06'],
        'C10' : ['C12', 'C08'],
        'C12' : ['C14', 'C10'],
        'C14' : ['C12', 'C13'],
        'C13' : ['C14', 'C11'],
        'C11' : ['C13', 'C09'],
        'C09' : ['C11', 'C07'],
        'C07' : ['C09', 'C05'],
        'C05' : ['C07', 'Desembarque Doméstico'],
        'Desembarque Doméstico' : ['C05', 'Refeitorio C', 'Estacionamento', 'Triagem Local', 'Elevador', 'B02'],
        'N107' : ['N106', 'C02'],
        'N106' : ['N108', 'N107'],
        'N108' : ['N105', 'N106'],
        'N105' : ['N109', 'N108'],
        'N109' : ['N104', 'N105'],
        'N104' : ['N110', 'N109'],
        'N110' : ['N103', 'N104'],
        'N103' : ['N111', 'N110'],
        'N111' : ['N102', 'N103'],
        'N102' : ['N101', 'N111'],
        'N101' : ['N102'],
        'M08' : ['N107', 'M07', 'C02'],
        'M07' : ['M08', 'M06'],
        'M06' : ['M07', 'M05'],
        'M05' : ['M06', 'M04'],
        'M04' : ['M05', 'M03'],
        'M03' : ['M04', 'M02'],
        'M02' : ['M03', 'M01'],
        'M01' : ['M02', 'R08', 'R19'],
        'R08' : ['M01', 'R19', 'R07'],
        'R07' : ['R08', 'R06'],
        'R06' : ['R07', 'R05'],
        'R05' : ['R06', 'R04'],
        'R04' : ['R05', 'R03'],
        'R03' : ['R04', 'R02'],
        'R02' : ['R03', 'R01'],
        'R01' : ['R02', 'R09', 'T0'],
        'T0' : ['R01'],
        'R09' : ['R19', 'R10', 'R01'],
        'R10' : ['R11', 'T05', 'R09'],
        'R11' : ['R12', 'R10'],
        'R12' : ['R13', 'R11'],
        'R13' : ['R12', 'T01'],
        'R19' : ['R18', 'R09', 'R08', 'M01'],
        'R18' : ['R19', 'R17'],
        'R17' : ['R18', 'R16'],
        'R16' : ['R17', 'R14', 'R15'],
        'R14' : ['R15', 'R18'],
        'R15' : ['R14', 'R18'],
        'T05' : ['R10', 'T04'],
        'T04' : ['T03', 'T05'],
        'T03' : ['T02', 'T04'],
        'T02' : ['T01', 'T03'],
        'T01' : ['R13', 'Hangar'],
        'Hangar' : ['T01']
    }

    for vertice in lista_adjacencias.keys():
        if 'Estacionamento' not in lista_adjacencias[vertice]:
            lista_adjacencias[vertice].append('Estacionamento')

    if 'Estacionamento' in lista_adjacencias:
        lista_adjacencias['Estacionamento'] = list(lista_adjacencias.keys())
    else:
        lista_adjacencias['Estacionamento'] = list(lista_adjacencias.keys())

    for node, neighbors in lista_adjacencias.items():
        for neighbor in neighbors:
            ponto1 = ponto_por_nome[node]
            ponto2 = ponto_por_nome[neighbor]
            distancia = calcular_distancia_manhattan(ponto1, ponto2)
            grafo.add_edge(node, neighbor, weight=distancia)

    return grafo