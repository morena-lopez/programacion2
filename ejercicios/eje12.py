def cifrado_cesar(texto, desplazamiento):
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for c in texto:
        
        if c in minus:
            pos = 0
            while pos < 26 and minus[pos] != c:
                pos += 1
            
            nueva_pos = (pos + desplazamiento) % 26
            resultado += minus[nueva_pos]

        
        elif c in mayus:
            pos = 0
            while pos < 26 and mayus[pos] != c:
                pos += 1
            nueva_pos = (pos + desplazamiento) % 26
            resultado += mayus[nueva_pos]

        
        else:
            resultado += c

    return resultado


# Ejemplo
mensaje = "HOLA MUNDO"
cifrado = cifrado_cesar(mensaje, 3)
print("Cifrado (+3):", cifrado)

descifrado = cifrado_cesar(cifrado, -3)
print("Descifrado (-3):", descifrado)
