import cv2
import numpy as np


path = "..\\images\\card.jpg"
image = cv2.imread(path)

# Grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur
image_blur = cv2.GaussianBlur(image, (7, 7), 0)

# Canny (imagem toda preta com um contorno branco nos detalhes)
image_canny = cv2.Canny(image, 100, 100)

# Dillation
kernel = np.ones((5, 5), np.uint8)  # Gera uma matriz de 5x5
image_dillation = cv2.dilate(image, kernel, iterations=1)

# Erosion
image_erosion = cv2.erode(image, kernel, iterations=1)

# Resize
image_resized = cv2.resize(image, (200, 200))

# Crop
image_cropped = image[200:300, 0:800]

# Show image
cv2.imshow("Image", image_cropped)
cv2.waitKey(0)
