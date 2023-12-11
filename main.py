#!/usr/bin/env python3
import sqlite3
from brain_module import ChatGPT
import json

def obtener_comentarios(id_producto=None, categoria=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if id_producto:
        query = "SELECT comentario FROM comentario WHERE id_producto = ?"
        cursor.execute(query, (id_producto,))
    elif categoria:
        query = """
        SELECT comentario.comentario 
        FROM comentario 
        JOIN producto ON comentario.id_producto = producto.id 
        WHERE producto.category = ?
        """
        cursor.execute(query, (categoria,))
    else:
        return "No se especificó un criterio de búsqueda válido."

    # Obtener los comentarios y convertirlos en una cadena separada por comas
    comentarios = cursor.fetchall()
    comentarios_str = ', '.join([com[0] for com in comentarios])

    conn.close()

    return comentarios_str

def get_response(response):

    response=json.loads(response)
    # Extraer los comentarios positivos, negativos y el resumen
    comentarios_positivos = response["positivo"]
    comentarios_negativos = response["negativo"]
    resumen = response["resumen"]

    # Imprimir los resultados
    print("Comentarios Positivos:")
    for comentario in comentarios_positivos:
        print("-", comentario)

    print("\nComentarios Negativos:")
    for comentario in comentarios_negativos:
        print("-", comentario)

    print("\nResumen:")
    print(resumen)

if  __name__ == "__main__":
    bot = ChatGPT()
    prompt="basado en estos comentarios, enlista y evalua las caracteristicas para saber la percepcion del cliente sobre los productos, dame la respuesta en formato JSON como este {positivo:, negativo:, resumen:} "
    
    comentarios=obtener_comentarios(categoria="Camisa")
    response = bot.request_openai(prompt+comentarios)
    get_response(response)

    comentarios=obtener_comentarios(id_producto=1)
    response = bot.request_openai(prompt+comentarios)
    get_response(response)