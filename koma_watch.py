import cv2
from PIL import Image

furigoma = cv2.imread("furigoma.jpg")
print (type(furigoma))



cv2.imshow("盤の様子",furigoma)
cv2.waitKey(0)