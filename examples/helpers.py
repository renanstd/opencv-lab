import cv2


def show_image(image):
    cv2.imshow("Press Q to close", image)
    key = cv2.waitKey(0)
    if key == ord("q"):
        cv2.destroyAllWindows()
