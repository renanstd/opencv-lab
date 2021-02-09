import cv2


IMAGES_DIR = "..\\images\\"


# Carregar uma imagem
image = cv2.imread(IMAGES_DIR + "card.jpg")
# Carregar uma imagem em tons de cinza
image = cv2.imread(IMAGES_DIR + "card.jpg", cv2.IMREAD_GRAYSCALE)
# Salvar uma cópia da imagem
# cv2.imwrite("name.png", image)

# Exibir imagem
cv2.imshow("Press Q to close", image)

# Manter a imagem aberta até que o "q" seja pressionado
key = cv2.waitKey(0)
if key == ord("q"):
    cv2.destroyAllWindows()
