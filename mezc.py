import random

# Función 'mezclar': recibe una frase en str,
# y la devuelve con las palabras mezcladas y
# separadas por guiones, tipo 'str'
def mezclar(frase):
    separador = '-'
    frase_lista = frase.split()
    random.shuffle(frase_lista)     # esta instrucción la mezcla
    palabras = separador.join(frase_lista)
    return palabras
