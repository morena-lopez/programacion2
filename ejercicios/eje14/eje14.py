import os
from PIL import Image
import matplotlib.pyplot as plt

# cambiar el directorio actual al del archivo .py
os.chdir(os.path.dirname(__file__))

# abrir imagen original
imagen = Image.open("imagen.jpg").convert("RGB")

ancho, alto = imagen.size
b_n = Image.new("L", (ancho, alto))

# convertir a escala de grises
for x in range(ancho):
    for y in range(alto):
        r, g, b = imagen.getpixel((x, y))
        gris = int((r + g + b) / 3)
        b_n.putpixel((x, y), gris)

# rotar horizontalmente
blancoNegro_rotada = Image.new("L", (ancho, alto))
for x in range(ancho):
    for y in range(alto):
        pixel = b_n.getpixel((x, y))
        blancoNegro_rotada.putpixel((ancho - 1 - x, y), pixel)

# mostrar ambas imágenes con matplotlib (sin Paint)
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(imagen)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Escala de grises y rotada")
plt.imshow(blancoNegro_rotada, cmap="gray")
plt.axis("off")

plt.show()
