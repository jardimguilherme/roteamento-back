import extractKml
import createGraph as graph
import tspDijskstra as tsp
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
# CORS(app)

@app.route('/gates', methods=['GET'])
@cross_origin()
def get_gates():
    # pontos = extrair_nomes_e_coordenadas(caminho_arquivo)

    # Retorna uma lista de portões disponíveis
    names = [ponto['nome'] for ponto in pontos]
    return jsonify(sorted(names))

@app.route('/route', methods=['POST'])
@cross_origin()
def get_route():
    
    # Recebe uma lista de portões na qual o primeiro é o portão de partida
    gates = request.json['gates']
    print(gates)
    start_gate = 'Estacionamento'
    
    # Calcula a melhor rota
    route = tsp.caixeiro_viajante(grafo, gates, start_gate)
    route.pop(0)
    
    return jsonify(route)


if __name__ == '__main__':
    caminho_arquivo = 'static/coordenadas.kml'
    pontos = extractKml.extrair_nomes_e_coordenadas(caminho_arquivo)
    grafo = graph.criar_grafo(pontos)
    app.run(debug=True)