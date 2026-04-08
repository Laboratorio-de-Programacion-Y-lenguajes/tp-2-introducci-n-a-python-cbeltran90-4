# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    # TU CÓDIGO AQUÍ
    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    # TU CÓDIGO AQUÍ
    palabras = texto.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return " ".join(palabras_capitalizadas)
    pass


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    # TU CÓDIGO AQUÍ
    vocales = "aeiou"
    contador = 0
    
    for letra in texto.lower():
        if letra in vocales:
            contador += 1
    
    return contador
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    # TU CÓDIGO AQUÍ
    resultado = []
    
    for caracter in texto:
        if caracter.isalpha():  # Solo si es letra
            # Determinar si es mayúscula o minúscula
            if caracter.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')
            
            # Aplicar desplazamiento con módulo 26 (tamaño del alfabeto)
            nueva_pos = (ord(caracter) - inicio + desplazamiento) % 26
            nuevo_caracter = chr(inicio + nueva_pos)
            resultado.append(nuevo_caracter)
        else:
            # No es letra: se mantiene igual
            resultado.append(caracter)
    
    return ''.join(resultado)
    pass
