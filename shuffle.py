import random   # módulo con funciones random
import mezc     # importamos nuestro módulo

CANTIDAD = 8

# Si uno empieza una línea con el símbolo # entonces el intérprete (python3) ignora esa línea
# A estas líneas se las llama comentarios y sirven para documentar y anotar el código

# Pedimos entrada del teclado
# El valor ingreso termina en la variable 'entrada', con tipo str
print("Ingresá una frase")
print("> ",end='')
frase_ingresada = input()

# Mezclamos las palabras y las volvemos a unir con la función mezclar, que importamos de mezc.py
for i in range(CANTIDAD):
    frase_mezclada = mezc.mezclar(frase_ingresada)
    print(frase_mezclada)
