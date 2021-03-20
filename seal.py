import numpy as np
from config import *

'''
=======================================================================================================================
Данный код служит для определения окружностей методом Хафа. Изображение было пропорционалоно уменьшено и с помощью 
HoughCircles произведена выборка подходящих окружностей для определения печати.
=======================================================================================================================
'''


def seal_func(image):
    new_w = 500 / image.shape[1]
    size = (500, int(image.shape[0] * new_w))
    resize_image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)

    output = resize_image.copy()
    gray = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.9, 90, param1=50, param2=30, minRadius=30, maxRadius=50)

    if circles is not None:
        circles = np.round(circles[0, :]).astype('int')

        for x, y, r in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)
            cv2.rectangle(output, (x - 45, y - 45), (x + 45, y + 45), (0, 0, 255), 2)

    cv2.imshow('result', output)
    cv2.waitKey(0)
    return
