import cv2
import numpy as np


path = "..\\images\\cards.jpg"
image = cv2.imread(path)

# Bordas da carta que iremos trabalhar
# Para descobrir esses valores, eu abri ela no paint e verifiquei
points = np.float32([
    [415, 460],
    [637, 505],
    [305, 773],
    [575, 826],
])

# Dimensões aproximadas da carta plana
width = 250
height = 350
reference_points = np.float32([
    [0 ,0],
    [width ,0],
    [0, height],
    [width ,height],
])

# Só pra garantir, desenhar círculos para mostrar estes pontos
for x in range(0, 4):
    cv2.circle(
        image,
        (points[x][0], points[x][1]),  # position
        5,  # radius
        (0, 0, 255),  # color
        cv2.FILLED,  # preenchimento
    )

# A magia acontece aqui
matrix = cv2.getPerspectiveTransform(points, reference_points)
output = cv2.warpPerspective(
    image,  # imagem que será modificada
    matrix,  # a matriz que montamos
    (width, height)  # dimensões finais da imagem
)

cv2.imshow("Imagem original", image)
cv2.imshow("Image", output)
cv2.waitKey(0)
