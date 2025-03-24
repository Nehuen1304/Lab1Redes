from flask import Flask, jsonify, request
import random

app = Flask(__name__)
peliculas = [
    {'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Acción'},
    {'id': 2, 'titulo': 'Star Wars', 'genero': 'Acción'},
    {'id': 3, 'titulo': 'Interstellar', 'genero': 'Ciencia ficción'},
    {'id': 4, 'titulo': 'Jurassic Park', 'genero': 'Aventura'},
    {'id': 5, 'titulo': 'The Avengers', 'genero': 'Acción'},
    {'id': 6, 'titulo': 'Back to the Future', 'genero': 'Ciencia ficción'},
    {'id': 7, 'titulo': 'The Lord of the Rings', 'genero': 'Fantasía'},
    {'id': 8, 'titulo': 'The Dark Knight', 'genero': 'Acción'},
    {'id': 9, 'titulo': 'Inception', 'genero': 'Ciencia ficción'},
    {'id': 10, 'titulo': 'The Shawshank Redemption', 'genero': 'Drama'},
    {'id': 11, 'titulo': 'Pulp Fiction', 'genero': 'Crimen'},
    {'id': 12, 'titulo': 'Fight Club', 'genero': 'Drama'}
]


def obtener_peliculas():
    return jsonify(peliculas)


def obtener_pelicula(id):
    # Lógica para buscar la película por su ID y devolver sus detalles
    pelicula_encontrada = next((i for i in peliculas if i['id'] == id), None)
    if peliculas is None:
        return jsonify({'error': 'Película no encontrada'}), 404
    return jsonify(pelicula_encontrada)


def agregar_pelicula():
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    peliculas.append(nueva_pelicula)
    print(peliculas)
    return jsonify(nueva_pelicula), 201


def actualizar_pelicula(id):
    # Lógica para buscar la película por su ID y actualizar sus detalles
    pelicula_actualizada = next((i for i in peliculas if p['id'] == id), None)
    if pelicula_actualizada is None:
        return jsonify({'error': 'Película no encontrada'}), 404
    
    pelicula_actualizada['titulo'] = request.json.get('titulo', pelicula_actualizada['titulo'])
    pelicula_actualizada['genero'] = request.json.get('genero', pelicula_actualizada['genero'])
    
    return jsonify(pelicula_actualizada)


def eliminar_pelicula(id):
    # Lógica para buscar la película por su ID y eliminarla
    pelicula = next((i for i in peliculas if i['id']==id), None)
    if pelicula is None:
        return jsonify({'error': 'Película no encontrada'}), 404
    return jsonify({'mensaje': 'Película eliminada correctamente'})


def obtener_nuevo_id():
    if len(peliculas) > 0:
        ultimo_id = peliculas[-1]['id']
        return ultimo_id + 1
    else:
        return 1
    
def obtener_peliculas_por_genero(genero):
    peliculas_por_genero = [i for i in peliculas if genero.lower() == i['genero'].lower()]
    if not peliculas_por_genero: 
        return jsonify({'error': 'Genero no encontrado'}), 404 
    return jsonify(peliculas_por_genero) 

def buscar_peliculas():
    coincidir = request.args.get('Escribeme','').lower()
    if not coincidir:
        return jsonify({'error': 'Debe proporcionar un término de búsqueda'}), 400
    coincidencias = [i for i in peliculas if coincidir in i['titulo'].lower()]
    return jsonify(coincidencias)

def sugerir_pelicula_aleatoria():
    if not peliculas:
        return jsonify({'error': 'No hay películas disponibles'}), 404
    return jsonify(random.choice(peliculas))

def sugerir_pelicula_por_genero(genero):
    peliculas_de_genero = [i for i in peliculas if i['genero'].lower() == genero.lower()]
    if not peliculas_de_genero:
        return jsonify({'error': 'No se encontraron peliculas de ese genero'}), 404
    return jsonify(peliculas_de_genero)


app.add_url_rule('/peliculas', 'obtener_peliculas', obtener_peliculas, methods=['GET'])
app.add_url_rule('/peliculas/<int:id>', 'obtener_pelicula', obtener_pelicula, methods=['GET'])
app.add_url_rule('/peliculas', 'agregar_pelicula', agregar_pelicula, methods=['POST'])
app.add_url_rule('/peliculas/<int:id>', 'actualizar_pelicula', actualizar_pelicula, methods=['PUT'])
app.add_url_rule('/peliculas/<int:id>', 'eliminar_pelicula', eliminar_pelicula, methods=['DELETE'])

if __name__ == '__main__':
    app.run()
