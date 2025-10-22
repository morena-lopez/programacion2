from PIL import Image
import matplotlib.pyplot as plt

# Función para convertir una imagen a escala de grises
def convertir_a_grises(img_color):
    # Crear una nueva imagen en RGB del mismo tamaño
    ancho, alto = img_color.size
    img_gris = Image.new("RGB", (ancho, alto))

    # Recorremos cada píxel
    for x in range(ancho):
        for y in range(alto):
            R, G, B = img_color.getpixel((x, y))  # obtener valores de color
            gris = int(R * 0.2989 + G * 0.5870 + B * 0.1140)  # fórmula dada
            img_gris.putpixel((x, y), (gris, gris, gris))  # asignar valor gris

    return img_gris


# --- Programa principal ---
# Cargar imagen (ej: "foto.jpg" debe estar en la misma carpeta que el script)
imagen_color = Image.open("images.jpg")

# Convertir a escala de grises
imagen_gris = convertir_a_grises(imagen_color)

# Mostrar imágenes lado a lado
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(imagen_color)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Escala de Grises")
plt.imshow(imagen_gris, cmap="gray")
plt.axis("off")

plt.show()
