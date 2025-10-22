from PIL import Image
import matplotlib.pyplot as plt

# --- Filtro Gaussiano 3x3 ---
kernel = [[1, 2, 1],
          [2, 4, 2],
          [1, 2, 1]]
factor = 16  # Normalización

# --- Función para aplicar convolución ---
def aplicar_filtro(img, kernel, factor):
    ancho, alto = img.size
    nueva_img = Image.new("RGB", (ancho, alto))
    pix = img.load()

    for x in range(1, ancho-1):   # evitamos bordes
        for y in range(1, alto-1):
            sumaR, sumaG, sumaB = 0, 0, 0

            # Recorrer kernel 3x3
            for i in range(3):
                for j in range(3):
                    px = pix[x + i - 1, y + j - 1]
                    k = kernel[j][i]
                    sumaR += px[0] * k
                    sumaG += px[1] * k
                    sumaB += px[2] * k

            # Normalizar y limitar a [0,255]
            r = min(255, max(0, int(sumaR / factor)))
            g = min(255, max(0, int(sumaG / factor)))
            b = min(255, max(0, int(sumaB / factor)))

            nueva_img.putpixel((x, y), (r, g, b))

    return nueva_img


# --- Programa principal ---
# Cargar imagen
imagen = Image.open("images.jpg")

# Aplicar filtro gaussiano
imagen_filtrada = aplicar_filtro(imagen, kernel, factor)

# Mostrar imágenes
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(imagen)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Gaussiano")
plt.imshow(imagen_filtrada)
plt.axis("off")

plt.show()
