from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("g.jpg")

print("¿Cómo querés rotar la imagen?")
print("1 - 90° a la derecha")
print("2 - 90° a la izquierda")
print("3 - 180°")

opcion = input("Elegí una opción (1/2/3): ")

def rotar_imagen(img, opcion):
    if opcion == "1":
        return img.transpose(Image.ROTATE_270)
    elif opcion == "2":
        return img.transpose(Image.ROTATE_90)
    elif opcion == "3":
        return img.transpose(Image.ROTATE_180)
    else:
        print("Opción inválida")
        return img

rotada = rotar_imagen(img, opcion)


plt.figure(figsize=(8,4))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Rotada")
plt.imshow(rotada)
plt.axis("off")

plt.show()
