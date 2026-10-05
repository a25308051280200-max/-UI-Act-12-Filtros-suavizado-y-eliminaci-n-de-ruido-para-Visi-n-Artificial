import cv2

# Cargar la imagen de entrada (formato .jfif)
imagen = cv2.imread("imagenes/pelicano_0200.jfif")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano", imagen_suavizada)

# Guardar resultado (usando extensión .jpg soportada por OpenCV)
cv2.imwrite(
    "resultados/pelicano_0200.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("resultados/pelicano_0200.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Alejandra Rivera Valenzuela NC 0200")