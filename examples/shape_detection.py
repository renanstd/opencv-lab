import cv2
import helpers
import numpy as np


frame_width = 640
frame_height = 480

capture = cv2.VideoCapture("http://192.168.1.32:4747/video")
capture.set(3, frame_width)
capture.set(4, frame_height)

def get_contours(image, image_contour):
    contours, hierarchy = cv2.findContours(
        image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )
    # Remover contornos zoados
    for contour in contours:
        # Pegar a área do contorno
        area = cv2.contourArea(contour)
        # Apenas considerar contornos com área grande
        if area > cv2.getTrackbarPos("Area", "Parameters"):
            # Desenhar contornos
            cv2.drawContours(
                image_contour,
                contour,
                -1,
                (255, 0, 255),
                7
            )
            # Calcular o perímetro do contorno
            perimeter = cv2.arcLength(contour, True)
            # Detectar os cantos aproximados deste contorno
            approximate = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            # Se o contorno tem 4 cantos, provavelmente ele é um quadrado ou retângulo
            # print(len(approximate))
            # Obter coordenadas do objeto encontrado em approximate
            x, y, width, height = cv2.boundingRect(approximate)
            # Desenhar um quadrado em volta do item detectado
            cv2.rectangle(
                image_contour,
                (x, y),
                (x + width, y + height),
                (0, 255, 0),
                5
            )
            # Adicionar um texto também, dos pontos
            cv2.putText(
                image_contour,
                "Points: " + str(len(approximate)),
                (x + y + 20, y + 20),
                cv2.FONT_HERSHEY_COMPLEX,
                .7,
                (0, 255, 0),
                2
            )
            # Adicionar um texto também, da área
            cv2.putText(
                image_contour,
                "Area: " + str(int(area)),
                (x + y + 20, y + 45),
                cv2.FONT_HERSHEY_COMPLEX,
                .7,
                (0, 255, 0),
                2
            )

# Cria uma telinha para regularmos ao vivo algumas configurações
def empty(a):
    pass
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 125, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 70, 255, empty)
cv2.createTrackbar("Area", "Parameters", 9000, 30000, empty)

while True:
    success, image = capture.read()

    # Aplicar um blur na imagem
    image_blur = cv2.GaussianBlur(image, (7, 7), 1)
    # Deixar em escala cinza
    image_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)
    # Aplicar canny
    # Buscar os valores de threshold da nossa telinha de config
    threshold_1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold_2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    image_canny = cv2.Canny(image_gray, threshold_1, threshold_2)
    # Aplica um dillation para evitar noises
    kernel = np.ones((5, 5))
    image_dillation = cv2.dilate(image_canny, kernel, iterations=1)
    # Localiza contornos
    image_contour = image.copy()
    get_contours(image_dillation, image_contour)

    # Exibir imagens em galeria com stack_images
    image_stack = helpers.stack_images(0.8, ([image, image_dillation, image_contour]))
    cv2.imshow("Result", image_stack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
