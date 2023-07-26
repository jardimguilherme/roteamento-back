from pykml import parser

def extrair_nomes_e_coordenadas(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        root = parser.parse(arquivo).getroot()

    pontos = []
    for placemark in root.Document.Placemark:
        nome = placemark.name.text.strip()
        coordenadas = placemark.Point.coordinates.text.strip()
        longitude, latitude, _ = map(float, coordenadas.split(','))
        pontos.append({'nome': nome, 'latitude': latitude, 'longitude': longitude})

    return pontos

def extrair_latitude_longitude(coordenadas):
    coordenadas = coordenadas.split(',')
    longitude, latitude = float(coordenadas[0]), float(coordenadas[1])
    return latitude, longitude
