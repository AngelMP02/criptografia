def atbash_cifrado(texto, alfabeto_original, alfabeto_cifrado):
    resultado = []
    for letra in texto:
        if letra in alfabeto_original:
            indice_original = alfabeto_original.index(letra)
            letra_cifrada = alfabeto_cifrado[indice_original]
            resultado.append(letra_cifrada)
        else:
            resultado.append(letra)
    return ''.join(resultado)

# Definir los alfabetos originales y cifrados para hebreo y español
alfabeto_hebreo_original = "נמלכיטחזוהדגבאתשרקצפעס"
alfabeto_hebreo_cifrado = "חטיכלמנסעפצקרשתאבגדהוז"

alfabeto_espanol_original = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_espanol_cifrado = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

# Ejemplo de cifrado con Atbash
texto_hebreo = "שלום"
cifrado_hebreo = atbash_cifrado(texto_hebreo, alfabeto_hebreo_original, alfabeto_hebreo_cifrado)
print("Texto cifrado en hebreo:", cifrado_hebreo)

texto_espanol = "holamundo"
cifrado_espanol = atbash_cifrado(texto_espanol, alfabeto_espanol_original, alfabeto_espanol_cifrado)
print("Texto cifrado en español:", cifrado_espanol)