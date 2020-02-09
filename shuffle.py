import random

print("Ingresame una frase wacho")
print("> ",end='')

def mezclar(frase):
    separador = '-'
    frasli = frase.split()
    random.shuffle(frasli)
    palabras = separador.join(frasli)
    return palabras

entrada = input()
primer = mezclar(entrada)

print("Primer shuffle: ")
print(primer)
print()

print("Los cinco:")
for i in range(5):
    print(mezclar(entrada))
