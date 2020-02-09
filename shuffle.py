import random

# Si uno empieza una línea con el
# símbolo # entonces el intérprete
# ignora esa línea

# A estas líneas se las llama comentarios
# y sirven para documentar y anotar el código

# Función 'mezclar': recibe una frase en str,
# y la devuelve con las palabras mezcladas y
# separadas por guiones, tipo 'str'
def mezclar(frase):
    separador = '-'
    frase_lista = frase.split()
    random.shuffle(frase_lista)     # esta instrucción la mezcla
    palabras = separador.join(frase_lista)
    return palabras


# Pedimos entrada del teclado
# El valor ingreso termina en la
# variable 'entrada', y con tipo str
print("Ingresá una frase")
print("> ",end='')
frase_ingresada = input()

frase_mezclada = mezclar(frase_ingresada)
print(frase_mezclada)
