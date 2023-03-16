from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
lista_pokemons={}


@app.route('/',methods=['GET'])
def index():
    exit()
    return '<h1>HOLA</h1>'

@app.route('/pokemons', methods=['GET'])
def all_pokemon():
    numero_pokemon = len(lista_pokemons)
    return make_response(jsonify({"found":numero_pokemon,"data":lista_pokemons}), 200)

@app.route('/pokemons', methods=['POST'])
def insert_pokemon():
    pokemon_map = request.json
    print(pokemon_map)
    for pokemon in pokemon_map:
        lista_pokemons[pokemon['nombre']] = pokemon
    return lista_pokemons

@app.route('/pokemons/<nombre>', methods=['PUT'])
def put_pokemon(nombre=None):
    for pokemon in lista_pokemons:

      if pokemon == nombre:
            lista_pokemons[nombre]["tipo"] = request.json['tipo']
            return lista_pokemons

    return make_response(jsonify({"message":"Pokemon not found"}), 404)

@app.route('/pokemons/<nombre>', methods=['DELETE'])
def delete_pokemon(nombre):
    for pokemon in lista_pokemons:

        if pokemon == nombre:
            del lista_pokemons[pokemon]
            return lista_pokemons

    return lista_pokemons

def main():
    app.run(host="0.0.0.0",port=5000, debug=False)

if __name__ == "__main__":
    main()