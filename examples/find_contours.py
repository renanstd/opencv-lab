import cv2
from helpers import show_image


IMAGES_DIR = "..\\images\\"


# Carregar uma imagem
original_image = cv2.imread(IMAGES_DIR + "card.jpg")
image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
# image = cv2.GaussianBlur(image, (5, 5), 0)
image = cv2.medianBlur(image, 5)

# https://docs.opencv.org/4.5.1/d7/d4d/tutorial_py_thresholding.html

# Para aplicar o threshold, a imagem deve estar em escala de cinza
retval, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

# Threshold adaptativo
# thresh = cv2.adaptiveThreshold(
#     image,
#     255,
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     cv2.THRESH_BINARY,
#     11,
#     7
# )
show_image(thresh)

# Detectar contornos
# https://docs.opencv.org/4.5.1/d4/d73/tutorial_py_contours_begin.html
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

# Desenhar contornos em uma imagem
image = cv2.drawContours(
    original_image,  # imagem
    contours,  # valores de contornos, obtidos com o findContours()
    -1,  # contour index, -1 desenha todos, de resto seque a ordem
    (255, 0, 0),  # cor do contorno
    2  # grossura do contorno
)

show_image(image)
